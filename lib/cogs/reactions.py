from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions
from discord import Embed
from datetime import datetime, timedelta
from discord.ext.commands import is_owner
from random import choice
from asyncio import sleep

from ..db import db

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

class Reactions(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.polls = []
		self.giveaways = []

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.starboard_channel = self.bot.get_channel(842341672868511744)
			self.bot.cogs_ready.ready_up("reactions")

	@command(name = "createpoll", aliases = ["mkpoll",])
	@is_owner()
	@has_permissions(manage_guild = True)
	async def createpoll_command(self, ctx, hours: int, question: str, *options):
		if len(options) > 10:
			await ctx.send("You can have a maximum of 10 options only.")
		else:
			embed = Embed(title = "Poll",
				          description = question,
				          colour=(0xa451d8),
				          timestamp = datetime.utcnow())

			embed.set_footer(text = "React to cast a vote.")
			fields = [("Options", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)]), False)]

			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)

			message = await ctx.send(embed=embed)

			for emoji in numbers[:len(options)]:
				await message.add_reaction(emoji)

			self.polls.append((message.channel.id, message.id))

			self.bot.scheduler.add_job(self.complete_poll, "date", run_date=datetime.now()+timedelta(seconds=hours*3600),
									   args=[message.channel.id, message.id])

	async def complete_poll(self, channel_id, message_id):
		message = await self.bot.get_channel(channel_id).fetch_message(message_id)

		most_voted = max(message.reactions, key=lambda r: r.count)

		await message.channel.send(f"The poll ended and {most_voted.emoji} got the highest votes with {most_voted.count - 1} votes.")
		self.polls.remove((message.channel.id, message.id))

	@createpoll_command.error
	async def createpoll_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Insufficient permissions to perform that task.")

	@command(name = "giveaway")
	@has_permissions(manage_guild = True)
	async def giveaway_command(self, ctx, hours: int, *, description: str):
		giveaway_embed = Embed(title = "Giveaway",
			                   description = description,
			                   colour=(0xa451d8),
				          	   timestamp = datetime.utcnow())

		fields = [("End Time", f"{datetime.utcnow() + timedelta(seconds = hours)} UTC", False)]

		for name, value, inline in fields:
			giveaway_embed.add_field(name=name, value=value, inline=inline)	

		message = await ctx.send(embed = giveaway_embed)
		await message.add_reaction("✅")	

		self.giveaways.append((message.channel.id, message.id))

		self.bot.scheduler.add_job(self.complete_giveaway, "date", run_date=datetime.now()+timedelta(seconds=hours),
								   args=[message.channel.id, message.id])

	async def complete_giveaway(self, channel_id, message_id):
		message = await self.bot.get_channel(channel_id).fetch_message(message_id)

		if len((entrants := [u for u in await message.reactions[0].users().flatten() if not u.bot])) > 0:
			winner = choice(entrants)

			while winner.top_role != None:
				await message.channel.send(f"The giveaway ended and the winner is... {winner.mention}! Congratulations 🎉")
				self.giveaways.remove((message.channel.id, message.id))
			else:
				winner = choice(entrants)

				await message.channel.send(f"The giveaway ended and the winner is... {winner.mention}! Congratulations 🎉")
				self.giveaways.remove((message.channel.id, message.id))

		else:
			await message.channel.send("The giveaway ended but no one turned up for it.")
			self.giveaways.remove((message.channel.id, message.id))

	@giveaway_command.error
	async def giveaway_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Insufficient permissions to perform that task.")

	# @command(name = "reroll")
	# async def reroll(self, ctx):
	# 	await self.reroll_command(channel_id, message_id)

	# async def reroll_command(self, channel_id, message_id):
	# 	message = await self.bot.get_channel(channel_id).fetch_message(message_id)

	# 	if len((entrants := [u for u in await message.reactions[0].users().flatten() if not u.bot])) > 0:
	# 		winner = choice(entrants)

	# 		await message.send(f"The new winner is... {winner.mention}! Congratulations 🎉")

	# 	else:
	# 		await message.channel.send("Could not find giveaway details in the database.")

	@Cog.listener()
	async def on_raw_reaction_add(self, payload):
		if self.bot.ready and payload.emoji.name == "⭐":
			message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

			if not message.author.bot and payload.member.id != message.author.id:
				msg_id, stars = db.record("SELECT StarMessageID, Stars FROM starboard WHERE RootMessageID = ?",
										  message.id) or (None, 0)

				embed = Embed(title="New Starred Message",
							  colour=(0xa451d8),
							  timestamp=datetime.utcnow())

				embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url_as(format='png'))

				fields = [("Author:", message.author.mention, False),
						  ("Content:", message.content or "See attachment", False),
						  ("Stars:", stars+1, False),
						  ("Original message:", message.jump_url, False)]

				for name, value, inline in fields:
					embed.add_field(name=name, value=value, inline=inline)

				if len(message.attachments):
					embed.set_image(url=message.attachments[0].url)

				if not stars:
					star_message = await self.starboard_channel.send(embed=embed)
					db.execute("INSERT INTO starboard (RootMessageID, StarMessageID) VALUES (?, ?)",
							   message.id, star_message.id)

				else:
					star_message = await self.starboard_channel.fetch_message(msg_id)
					await star_message.edit(embed=embed)
					db.execute("UPDATE starboard SET Stars = Stars + 1 WHERE RootMessageID = ?", message.id)

			else:
				await message.remove_reaction(payload.emoji, payload.member)

		elif payload.message_id in (poll[1] for poll in self.polls):
			message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

			for reaction in message.reactions:
				if (not payload.member.bot
					and payload.member in await reaction.users().flatten()
					and reaction.emoji != payload.emoji.name):
					await message.remove_reaction(reaction.emoji, payload.member)

def setup(bot):
	bot.add_cog(Reactions(bot))