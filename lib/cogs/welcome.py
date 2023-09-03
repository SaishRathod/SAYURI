from discord import Intents  
from discord import Forbidden
from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions, bot_has_permissions, has_role
from discord import Embed
from discord.ext.commands import is_owner
import asyncio
from asyncio import sleep

from ..db import db


class Welcome(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("welcome")
			self.wng_bots_harem = self.bot.get_channel(804219049377923092)
			self.wng_scbds = self.bot.get_channel(879768732547829810)  

	@command(name = "Join GIF setter", aliases = ["jgs",])
	@has_permissions(administrator = True)
	@is_owner()
	async def join_gif_setter(self, ctx, link):
		db.execute("UPDATE welcome SET Link = ? WHERE GuildID = ?", link, ctx.author.guild.id)
		await ctx.send("Adding link to the database, this will only take a minute or two.")
		await sleep(60)
		await ctx.send("Successfully added the link to the database.")

	@command(name = "Join message setter", aliases = ["jms",])
	@has_permissions(administrator = True)
	@is_owner()
	async def join_message_setter(self, ctx, *, message):
		db.execute("UPDATE welcome SET Message = ? WHERE GuildID = ?", message, ctx.author.guild.id)
		await ctx.send("Adding message to the database, this will only take a minute or two.")
		await sleep(60)
		await ctx.send("Successfully added the message to the database.")

	@command(name = "Leave GIF setter", aliases = ["lgs",])
	@is_owner()
	async def leave_gif_setter(self, ctx, link):
		db.execute("UPDATE leave SET Link = ? WHERE GuildID = ?", link, ctx.author.guild.id)
		await ctx.send("Adding link to the database, this will only take a minute or two.")
		await sleep(60)
		await ctx.send("Successfully added the link to the database.")

	@command(name = "Leave message setter", aliases = ["lms",])
	@has_permissions(administrator = True)
	@is_owner()
	async def leave_message_setter(self, ctx, *, message):
		db.execute("UPDATE leave SET Message = ? WHERE GuildID = ?", message, ctx.author.guild.id)
		await ctx.send("Adding message to the database, this will only take a minute or two.")
		await sleep(60)
		await ctx.send("Successfully added the message to the database.")

	@Cog.listener()
	async def on_member_join(self, member):
		join_gif = db.field("SELECT Link FROM welcome WHERE GuildID = ?", member.guild.id)
		join_message = db.field("SELECT Message FROM welcome WHERE GuildID = ?", member.guild.id)
		if member.guild.id == 774009780913045524: #BOTS HAREM
			if member.name == "Quasar" and member.discriminator == "7701":
				db.execute("INSERT INTO exp (UserID) VALUES (?)", member.id)
				embed = Embed(title = f"{member.name}#{member.discriminator} joined!!!",
					          description = join_message,
					          color = (0xa451d8))
				embed.set_image(url = join_gif)
				embed.set_thumbnail(url = member.avatar_url)
				await self.wng_bots_harem.send(embed = embed)
				await member.edit(roles = [*member.roles, *[member.guild.get_role(id_) for id_ in (804001953980874752,)]])      #ADD A FUCKIN COMMA EVEN IF THERE IS ONLY ONE ROLE

				try:
					await member.send(f"Welcome back Nova-kun!!! Still working eh?")

				except Forbidden:
					pass

			elif member.bot:
				embed = Embed(title = f"A Fellow Bot joined!",
					          description = f"Welcome to the server **{member.name}**! Hope you are a great help to Nova-kun.",
							  color = (0xa451d8))
				embed.set_image(url = "https://media1.tenor.com/images/72c9b849aa10b222371ebb99a6b1896a/tenor.gif?itemid=8807701")
				embed.set_thumbnail(url = member.avatar_url)

				await self.wng_bots_harem.send(embed = embed)
				await member.edit(roles = [*member.roles, *[member.guild.get_role(id_) for id_ in (866043005777215488,)]])

			else:
				db.execute("INSERT INTO exp (UserID) VALUES (?)", member.id)
				embed = Embed(title = f"{member.name}#{member.discriminator} joined!!!",
					          description = join_message,
					          color = (0xa451d8))
				embed.set_image(url = join_gif)
				embed.set_thumbnail(url = member.avatar_url)
				await self.wng_bots_harem.send(embed = embed)
				await member.edit(roles = [*member.roles, *[member.guild.get_role(id_) for id_ in (804586858746871818,)]])

				try:
					await member.send(f"Welcome to **{member.guild.name}** {member.mention}! Have fun!")

				except Forbidden:
					pass

		elif member.guild.id == 810740878187823134:   #SCBDS
			if member.bot:
				embed = Embed(title = f"A Fellow Bot joined!",
					          description = f"Welcome to the server **{member.name}**! Hope you are a great help to Nova-kun.",
							  color = (0xa451d8))
				embed.set_image(url = "https://media1.tenor.com/images/72c9b849aa10b222371ebb99a6b1896a/tenor.gif?itemid=8807701")
				embed.set_thumbnail(url = member.avatar_url)

				await self.wng_scbds.send(embed = embed)

			else:
				embed = Embed(title = f"{member.name}#{member.discriminator} joined!!!",
					          description = join_message,
					          color = (0xa451d8))
				embed.set_image(url = join_gif)
				embed.set_thumbnail(url = member.avatar_url)
				embed.set_footer(text = "This server is owned by SuperNova#5524.")
				await self.wng_scbds.send(embed = embed)
				await member.edit(roles = [*member.roles, *[member.guild.get_role(id_) for id_ in (810745963227512842, 813506849789050880, 873760925994344519,)]])

				try:
					await member.send(f"Welcome to **{member.guild.name}** {member.mention}! Enjoy your stay!")

				except Forbidden:
					pass

	@Cog.listener()
	async def on_member_remove(self, member):
		leave_gif = db.field("SELECT Link FROM leave WHERE GuildID = ?", member.guild.id)
		leave_message = db.field("SELECT Message FROM leave WHERE GuildID = ?", member.guild.id)
		if member.guild.id == 774009780913045524:
			if member.bot:
				embed = Embed(title = "Bot left.",
					          description = f"{member.name} is no longer with us...",
					          color = (0xa451d8))

				embed.set_image(url = "https://media1.tenor.com/images/8bbf9194008e3f8f2f2665c2cbe8dbca/tenor.gif?itemid=10837648")
				embed.set_thumbnail(url = member.avatar_url)

				await self.wng_bots_harem.send(embed = embed)

			else:
				db.execute("DELETE FROM exp WHERE UserID = ?", member.id)
				embed = Embed(title = f"{member.name}#{member.discriminator} left...",
					          description = leave_message,
					          color = (0xa451d8))
				embed.set_image(url = leave_gif)
				embed.set_thumbnail(url = member.avatar_url)
				await self.wng_bots_harem.send(embed = embed)

		elif member.guild.id == 810740878187823134:
			if member.bot:
				embed = Embed(title = "Bot left.",
					          description = f"{member.name} is no longer with us...",
					          colour = (0xa451d8))

				embed.set_image(url = "https://media1.tenor.com/images/8bbf9194008e3f8f2f2665c2cbe8dbca/tenor.gif?itemid=10837648")
				embed.set_thumbnail(url = member.avatar_url)

				await self.wng_scbds.send(embed = embed)

			else:
				db.execute("DELETE FROM exp WHERE UserID = ?", member.id)
				embed = Embed(title = f"{member.name}#{member.discriminator} left...",
							  description = leave_message,
					          color = (0xa451d8))
				embed.set_image(url = leave_gif)
				embed.set_thumbnail(url = member.avatar_url)
				await self.wng_scbds.send(embed = embed)

def setup(bot):
	bot.add_cog(Welcome(bot))