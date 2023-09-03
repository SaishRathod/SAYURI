import asyncio
import random
from asyncio import sleep
from datetime import datetime, timedelta
from re import search
from typing import Optional
from better_profanity import profanity
from discord import Embed, Member, NotFound, Object
from discord.utils import find
from discord.errors import HTTPException, Forbidden
from discord import DMChannel
from discord.ext.commands import is_owner
from discord.ext.commands import Cog, Greedy, Converter
from discord.ext.commands import CheckFailure, BadArgument
from discord.ext.commands import command, has_permissions, bot_has_permissions, has_role
from discord import TextChannel

from ..db import db


class BannedUser(Converter):
	async def convert(self, ctx, arg):
		if ctx.guild.me.guild_permissions.ban_members:
			if arg.isdigit():
				try:
					return (await ctx.guild.fetch_ban(Object(id=int(arg)))).user

				except NotFound:
					raise BadArgument


		banned = [e.user for e in await ctx.guild.bans()]
		if banned:
			if (user:= find(lambda u: str(u) == arg, banned)) is not None:
				return user
			else:
				raise BadArgument


class Mod(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.owner = "<@424486126351417344>"
		self.url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
		self.links_not_allowed = ()
		self.images_not_allowed = ()
		self.spam_allowed = (823778171803271199,)


	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.mute_role = self.bot.guild.get_role(800454660729208864)
			self.muted_channel = self.bot.get_channel(811462240363872276)
			self.modmail = self.bot.get_channel(806809187228450856)
			self.log_channel = self.bot.get_channel(800881621066448976)
			self.bot.cogs_ready.ready_up("mod")

		while True:
			with open("./data/spam_detect.txt", "r+") as file:
				await asyncio.sleep(10)
				file.truncate(0)

	async def kick_members(self, message, targets, reason):
		for target in targets:
			try:
				await target.send(f"You've been kicked from **{target.guild.name}** for reason: `{reason}`.")

			except Forbidden:
				pass

			except HTTPException:
				pass

			await target.kick(reason=reason)

			embed = Embed(title = "Member Kicked",
				          color = (0xa451d8),
				          timestamp = datetime.utcnow())

			embed.set_thumbnail(url = target.avatar_url)

			fields = [("Member:", f"{target.mention} aka {target.display_name}", False),
			          ("Kicked by:", message.author.mention, False),
			          ("Reason:", reason, False)]

			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)

			await self.log_channel.send(embed = embed)

	@command(name = "kick", brief= "Kick members from the server. They'll be able to join later through an invite.")
	@bot_has_permissions(kick_members = True)
	@has_permissions(kick_members = True)
	@is_owner()
	async def kick_command(self, ctx, targets: Greedy[Member], *, reason: Optional[str] = "No reason provided"):
		for target in targets:
			if not len(targets):
				await ctx.send("I cant find the member(s) in the server.")

			elif (ctx.guild.me.top_role.position > target.top_role.position and not target.guild_permissions.administrator and target != ctx.author and ctx.author.top_role.position > target.top_role.position):
				await self.kick_members(ctx.message, targets, reason)
				await ctx.send(f"Successfully kicked the member(s).")

			else:
				await ctx.send(f"Unable to execute command. This may be due to the following possibilities:\n1. The mentioned member's top role is above the user's top role.\n2. The mentioned member's top role is above my top role.\n3. The mentioned member is an administrator.\n||4. You mentioned yourself. If thats the case, I suppose that was a mistake ^^;||")

	@kick_command.error
	async def kick_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")

	async def ban_members(self, message, targets, reason):
		for target in targets:
			try:
				await target.send(f"You've been banned from **{target.guild.name}** for reason: `{reason}`.")

			except Forbidden:
				pass

			except HTTPException:
				pass
			
			await target.ban(reason=reason)

			embed = Embed(title = "Member Banned",
					      color = (0xa451d8),
					      timestamp = datetime.utcnow())

			embed.set_thumbnail(url = target.avatar_url)

			fields = [("Member:", f"{target.mention} aka {target.display_name}", False),
			          ("Banned by:", message.author.mention, False),
			          ("Reason:", reason, False)]

			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)

			await self.log_channel.send(embed = embed)

	@command(name = "ban", brief = "Ban members from the server.")
	@bot_has_permissions(ban_members = True)
	@has_permissions(ban_members = True)
	@is_owner()
	async def ban_command(self, ctx, targets: Greedy[Member], *, reason : Optional[str] = "No reason provided"):
		for target in targets:
			if not len(targets):
				await ctx.send("I cant find the member(s) in the server.")

			elif (ctx.guild.me.top_role.position > target.top_role.position and not target.guild_permissions.administrator and target != ctx.author and ctx.author.top_role.position > target.top_role.position):
				await self.ban_members(ctx.message, targets, reason)
				await ctx.send(f"Successfully banned the member(s).")

			else:
				await ctx.send(f"Unable to execute command. This may be due to the following possibilities:\n1. The mentioned member's top role is above the user's top role.\n2. The mentioned member's top role is above my top role.\n3. The mentioned member is an administrator.\n||4. You mentioned yourself. If thats the case, I suppose that was a mistake ^^;||")

	@ban_command.error
	async def ban_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")


	@command(name="unban")
	@bot_has_permissions(ban_members=True)
	@has_permissions(ban_members=True)
	@is_owner()
	async def unban_command(self, ctx, targets: Greedy[BannedUser], *, reason: Optional[str] = "No reason provided."):
		if not len(targets):
			await ctx.send("Couldn't find the member in the banned list.")

		else:
			for target in targets:
				await ctx.guild.unban(target, reason=reason)

				embed = Embed(title="Member Unbanned",
							  colour=(0xa451d8),
							  timestamp=datetime.utcnow())

				embed.set_thumbnail(url=target.avatar_url)

				fields = [("Member:", target.name, False),
						  ("Actioned by:", ctx.author.display_name, False),
						  ("Reason:", reason, False)]

				for name, value, inline in fields:
					embed.add_field(name=name, value=value, inline=inline)

				await self.log_channel.send(embed=embed)

			await ctx.send("Successfully unbanned the member(s).")

	@unban_command.error
	async def unban_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")

	@command(name = "clear", aliases = ["purge"], brief = "Clears a given amount of messages from the server or the server member.")
	@bot_has_permissions(manage_messages = True)
	@has_permissions(manage_messages = True)
	@is_owner()
	async def clear_messages(self, ctx, targets: Greedy[Member], limit: Optional[int] = 1):
		def _check(message):
			return not len(targets) or message.author in targets

		if 0 < limit <= 200:
			with ctx.channel.typing():
				await ctx.message.delete()
				deleted = await ctx.channel.purge(limit = limit, after = datetime.utcnow() - timedelta(days = 14), check = _check)

				await ctx.send(f"Deleted {len(deleted):,} messages.", delete_after = 5)

		else:
			await ctx.send("I cannot delete that many messages at a single time.")

	@clear_messages.error
	async def clear_messages_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")

	async def mute_members(self, message, targets, minutes, reason):
		unmutes = []

		for target in targets:
			if not self.mute_role in target.roles:
				role_ids = ",".join([str(r.id) for r in target.roles])
				end_time = datetime.utcnow() + timedelta(seconds=minutes*60) if minutes else None

				db.execute("INSERT INTO mutes VALUES (?, ?, ?)",
						   target.id, role_ids, getattr(end_time, "isoformat", lambda: None)())

				await target.edit(roles=[self.mute_role])

				embed = Embed(title="Member Muted",
							  colour=(0xa451d8),
							  timestamp=datetime.utcnow())

				embed.set_thumbnail(url=target.avatar_url)

				fields = [("Member:", target.display_name, False),
						  ("Actioned by:", message.author.display_name, False),
						  ("Duration:", f"{minutes:,} minute(s)" if minutes else "Indefinite", False),
						  ("Reason:", reason, False)]

				for name, value, inline in fields:
					embed.add_field(name=name, value=value, inline=inline)

				await self.log_channel.send(embed=embed)

				if minutes:
					unmutes.append(target)

		return unmutes

	@command(name="mute", brief = "Mute members in the server. You can also specify the time duration for the mute and I'll unmute them according to it.")
	@bot_has_permissions(manage_roles=True)
	@has_permissions(kick_members = True)
	@is_owner()
	async def mute_command(self, ctx, targets: Greedy[Member], minutes: Optional[int], *,
						   reason: Optional[str] = "No reason provided."):
		for target in targets:
			if not len(targets):
				await ctx.send("One or more required arguments are missing.")

			elif (ctx.guild.me.top_role.position > target.top_role.position and not target.guild_permissions.administrator and target != ctx.author and ctx.author.top_role.position > target.top_role.position):
				unmutes = await self.mute_members(ctx.message, targets, minutes, reason)
				await ctx.send("Successfully muted the member(s).")

				if len(unmutes):
					await sleep(minutes*60)
					await self.unmute_members(ctx.guild, targets)
			
			else:
				await ctx.send(f"Unable to execute command. This may be due to the following possibilities:\n1. The mentioned member's top role is above the user's top role.\n2. The mentioned member's top role is above my top role.\n3. The mentioned member is an administrator.\n||4. You mentioned yourself. If thats the case, I suppose that was a mistake ^^;||")

	@mute_command.error
	async def mute_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")

	async def unmute_members(self, guild, targets, *, reason="Mute time expired."):
		for target in targets:
			if self.mute_role in target.roles:
				role_ids = db.field("SELECT RoleIDs FROM mutes WHERE UserID = ?", target.id)
				roles = [guild.get_role(int(id_)) for id_ in role_ids.split(",") if len(id_)]

				db.execute("DELETE FROM mutes WHERE UserID = ?", target.id)

				await target.edit(roles=roles)

				embed = Embed(title="Member Unmuted",
							  colour=(0xa451d8),
							  timestamp=datetime.utcnow())

				embed.set_thumbnail(url=target.avatar_url)

				fields = [("Member:", target.display_name, False),
						  ("Reason:", reason, False)]

				for name, value, inline in fields:
					embed.add_field(name=name, value=value, inline=inline)

				await self.log_channel.send(embed=embed)

	@command(name="unmute", brief = "Unmute members in the server.")
	@bot_has_permissions(manage_roles=True)
	@has_permissions(kick_members = True)
	@is_owner()
	async def unmute_command(self, ctx, targets: Greedy[Member], *, reason: Optional[str] = "No reason provided."):
		for target in targets:
			if not len(targets):
				await ctx.send("One or more required arguments is missing.")

			elif (ctx.guild.me.top_role.position > target.top_role.position and not target.guild_permissions.administrator and target != ctx.author and ctx.author.top_role.position > target.top_role.position):
				await self.unmute_members(ctx.guild, targets, reason=reason)
				await ctx.send("Successfully unmuted the member(s).")

			else:
				await ctx.send(f"Unable to execute command. This may be due to the following possibilities:\n1. The mentioned member's top role is above the user's top role.\n2. The mentioned member's top role is above my top role.\n3. The mentioned member is an administrator.\n||4. You mentioned yourself. If thats the case, I suppose that was a mistake ^^;||")

	@unmute_command.error
	async def unmute_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")


	async def warn_members(self, message, target, *, reason):

			NoOfWarns = db.field("SELECT NoOfWarns FROM warnings WHERE UserID = ?", target.id)

			if NoOfWarns == 0:
				db.execute("UPDATE warnings SET NoOfWarns = ?,  R1 = ?, R1_Mod = ?, R1_Date = ? WHERE UserID = ?", 
					        NoOfWarns + 1, reason, message.author.name + "#" + message.author.discriminator, datetime.utcnow(), target.id)
				NoOfWarns += 1
				await message.send(f"Successfully warned `{target.name}` for: {reason}\nWarn Number: {NoOfWarns}/5")

			elif NoOfWarns == 1:
				db.execute("UPDATE warnings SET NoOfWarns = ?,  R2 = ?, R2_Mod = ?, R2_Date = ? WHERE UserID = ?", 
					        NoOfWarns + 1, reason, message.author.name + "#" + message.author.discriminator, datetime.utcnow(), target.id)
				NoOfWarns += 1
				await message.send(f"Successfully warned `{target.name}` for: {reason}\nWarn Number: {NoOfWarns}/5")

			elif NoOfWarns == 2:
				db.execute("UPDATE warnings SET NoOfWarns = ?,  R3 = ?, R3_Mod = ?, R3_Date = ? WHERE UserID = ?", 
					        NoOfWarns + 1, reason, message.author.name + "#" + message.author.discriminator, datetime.utcnow(), target.id)
				NoOfWarns += 1
				await message.send(f"Successfully warned `{target.name}` for: {reason}\nWarn Number: {NoOfWarns}/5")

			elif NoOfWarns == 3:
				db.execute("UPDATE warnings SET NoOfWarns = ?,  R4 = ?, R4_Mod = ?, R4_Date = ? WHERE UserID = ?", 
					        NoOfWarns + 1, reason, message.author.name + "#" + message.author.discriminator, datetime.utcnow(), target.id)
				NoOfWarns += 1
				await message.send(f"Successfully warned `{target.name}` for: {reason}\nWarn Number: {NoOfWarns}/5")

			elif NoOfWarns == 4:
				db.execute("UPDATE warnings SET NoOfWarns = ?,  R5 = ?, R5_Mod = ?, R5_Date = ? WHERE UserID = ?", 
					        NoOfWarns + 1, reason, message.author.name + "#" + message.author.discriminator, datetime.utcnow(), target.id)
				NoOfWarns += 1
			
				await message.send(f"Successfully warned `{target.name}` for: {reason}\nWarn Number: {NoOfWarns}/5")

			else:
				await message.send(f"Warn limit reached: `{target.name}` has been warned 5 times already. \n(Contact SuperNova for more info.)")


	@command(name = "warn", brief = "Warn a member.")
	@bot_has_permissions(kick_members = True)
	@has_permissions(kick_members = True)
	@is_owner()
	async def warn_command(self, ctx, target: Member, *, reason):

		if (ctx.guild.me.top_role.position > target.top_role.position and not target.guild_permissions.administrator and target != ctx.author and ctx.author.top_role.position > target.top_role.position):
			await self.warn_members(ctx, target, reason = reason)
		
			warn_embed = Embed(title="Member Warned",
						  colour=(0xa451d8),
						  timestamp=datetime.utcnow())

			warn_embed.set_thumbnail(url=target.avatar_url)

			fields = [("Member:", target.name, False),
					  ("Actioned by:", ctx.author.display_name, False),
					  ("Reason:", reason, False)]

			for name, value, inline in fields:
				warn_embed.add_field(name=name, value=value, inline=inline)

			await self.log_channel.send(embed = warn_embed)

			try:
				await target.send(f"You have been warned in **{ctx.guild.name}** for: `{reason}`")

			except Forbidden:
				pass

		else:
			await ctx.send(f"Unable to execute command. This may be due to the following possibilities:\n1. The mentioned member's top role is above the user's top role.\n2. The mentioned member's top role is above my top role.\n3. The mentioned member is an administrator.\n||4. You mentioned yourself. If thats the case, I suppose that was a mistake ^^;||")

	@warn_command.error
	async def warn_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")


	@command(name = "warnings", aliases = ["warns",], brief = "Displays the warnings of a member.")
	@is_owner()
	async def warnings_command(self, ctx, target: Optional[Member]):
		target = target or ctx.author

		NoOfWarns = db.field("SELECT NoOfWarns FROM warnings WHERE UserID = ?", target.id)

		R1 = db.field("SELECT R1 FROM warnings WHERE UserID = ?", target.id)
		R1_Mod = db.field("SELECT R1_Mod FROM warnings WHERE UserID = ?", target.id)
		R1_Date = db.field("SELECT R1_Date FROM warnings WHERE UserID = ?", target.id)
		R2 = db.field("SELECT R2 FROM warnings WHERE UserID = ?", target.id)
		R2_Mod = db.field("SELECT R2_Mod FROM warnings WHERE UserID = ?", target.id)
		R2_Date = db.field("SELECT R2_Date FROM warnings WHERE UserID = ?", target.id)
		R3 = db.field("SELECT R3 FROM warnings WHERE UserID = ?", target.id)
		R3_Mod = db.field("SELECT R3_Mod FROM warnings WHERE UserID = ?", target.id)
		R3_Date = db.field("SELECT R3_Date FROM warnings WHERE UserID = ?", target.id)
		R4 = db.field("SELECT R4 FROM warnings WHERE UserID = ?", target.id)
		R4_Mod = db.field("SELECT R4_Mod FROM warnings WHERE UserID = ?", target.id)
		R4_Date = db.field("SELECT R4_Date FROM warnings WHERE UserID = ?", target.id)
		R5 = db.field("SELECT R5 FROM warnings WHERE UserID = ?", target.id)
		R5_Mod = db.field("SELECT R5_Mod FROM warnings WHERE UserID = ?", target.id)
		R5_Date = db.field("SELECT R5_Date FROM warnings WHERE UserID = ?", target.id)

		warns_embed = Embed(title = f"Warnings - {target.name}:",
							description = f"**Total warns: {NoOfWarns}**",
			                colour=(0xa451d8))

		fields = [("1.",R1, True),
		          ("Warned by:", R1_Mod, True),
		          ("On:", R1_Date, True),
		          ("2.", R2, True),
		          ("Warned by:", R2_Mod, True),
		          ("On:", R2_Date, True),
				  ("3.", R3, True),
		          ("Warned by:", R3_Mod, True),
		          ("On:", R3_Date, True),
				  ("4.", R4, True),
		          ("Warned by:", R4_Mod, True),
		          ("On:", R4_Date, True),
				  ("5.", R5, True),
		          ("Warned by:", R5_Mod, True),
		          ("On:", R5_Date, True)]

		warns_embed.set_thumbnail(url = target.avatar_url)
		warns_embed.set_footer(text = "*All dates and times are shown in UTC.")

		for name, value, inline in fields:
					warns_embed.add_field(name=name, value=value, inline=inline)

		await ctx.send(embed = warns_embed)


	@command(name = "clearwarnings", aliases = ["clw", "clearwarns"], brief = "Clear all the warnings of a member.")
	@bot_has_permissions(kick_members = True)
	@has_permissions(administrator = True)
	@is_owner()
	async def clear_warnings_command(self, ctx, target:Member):

		db.execute("UPDATE warnings SET NoOfWarns = ?, R1 = ?, R1_Mod = ?,R1_Date = ?, R2 = ?, R2_Mod = ?, R2_Date = ?, R3 = ?, R3_Mod = ?, R3_Date = ?, R4 = ?, R4_Mod = ?,R4_Date = ?, R5 = ?, R5_Mod = ?,R5_Date = ? WHERE UserID = ?", 
			        0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, target.id)

		await ctx.send("Successfully cleared all the warnings.")

		log_embed = Embed(title = "Warnings Cleared",
			              colour = (0xa451d8),
			              timestamp=datetime.utcnow())

		fields = [("For:", target.mention, False),
				  ("By:", ctx.author, False)]	

		log_embed.set_thumbnail(url = target.avatar_url)

		for name, value, inline in fields:
			log_embed.add_field(name=name, value=value, inline=inline)

		await self.log_channel.send(embed = log_embed)

	@clear_warnings_command.error
	async def clear_warnings_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")


	# @command(name = "lockdown", brief = "Put a channel on lockdown so the members cannot send messages. Useful during raids.")
	# @bot_has_permissions(manage_channels = True)
	# @has_permissions(manage_channels = True)
	# @is_owner()
	# async def lockdown(self, ctx, TextChannel = None):
	# 	channel = TextChannel or ctx.channel

	# 	if ctx.guild.default_role not in channel.overwrites:
	# 		overwrites = {
	# 		ctx.guild.default_role : discord.PermissionOverwrite(send_messages = False)
	# 		}
	# 		await channel.edit(overwrites = overwrites)
	# 		await ctx.send(f"{ctx.author.mention} has put `{channel.name}` on lockdown.")
	# 	elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
	# 		overwrites = channel.overwrites[ctx.guild.default_role]
	# 		overwrites.send_messages = False
	# 		await channel.set_permissions(ctx.guild.default_role, overwrite = overwrites)
	# 		await ctx.send(f"{ctx.author.mention} has put `{channel.name}` on lockdown.")
	# 	else:
	# 		overwrites = channel.overwrites[ctx.guild.default_role]
	# 		overwrites.send_messages = True
	# 		await channel.set_permissions(ctx.guild.default_role, overwrite = overwrites)
	# 		await ctx.send(f"{ctx.author.mention} has removed `{channel.name}` from lockdown.")

	# 	embed = Embed(title="Channel on Lockdown",
	# 						  colour=(0xa451d8),
	# 						  timestamp=datetime.utcnow())


	# 	fields = [("Actioned by:", ctx.author.name, False),
	# 			  ("On channel:", channel, False)]

	# 	embed.set_thumbnail(url= ctx.guild.icon_url)

	# 	for name, value, inline in fields:
	# 		embed.add_field(name=name, value=value, inline=inline)

	# 	await self.log_channel.send(embed=embed)


	@command(name = "addbanword", aliases=["addswearword"], brief= "Add a new word to the banned list to be censored in the future.")
	@has_permissions(manage_guild = True)
	@is_owner()
	async def add_profanity(self, ctx, *words):
		with open("./data/profanity.txt", "a", encoding = "utf-8") as f:
			f.write("".join([f"{w}\n" for w in words]))

		profanity.load_censor_words_from_file("./data/profanity.txt")
		await ctx.send("Successfully added the word(s) to database.")

	@add_profanity.error
	async def add_profanity_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")

	@command(name="delbanword", aliases=["delswearword"], brief= "Remove an existing word from the banned word list.")
	@has_permissions(manage_guild=True)
	@is_owner()
	async def remove_profanity(self, ctx, *words):
		with open("./data/profanity.txt", "r", encoding="utf-8") as f:
			stored = [w.strip() for w in f.readlines()]

		with open("./data/profanity.txt", "w", encoding="utf-8") as f:
			f.write("".join([f"{w}\n" for w in stored if w not in words]))

		profanity.load_censor_words_from_file("./data/profanity.txt")
		await ctx.send("Successfully removed the word(s) from database.")

	@remove_profanity.error
	async def remove_profanity_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")

	@command(name = "display profanity", aliases = ["profanities", "bl"])
	async def display_profanity_command(self, ctx):
		with open("./data/profanity.txt", "r", encoding = "utf-8") as f:
			profanities = f.read()

			display_profanity_embed = Embed(description = profanities,
			              					colour = (0xa451d8),
			              					timestamp=datetime.utcnow())


			display_profanity_embed.set_author(name = "Here's a list of all the banned words:", icon_url = ctx.me.avatar_url)
			display_profanity_embed.set_thumbnail(url = ctx.guild.icon_url)

			await ctx.send(embed = display_profanity_embed)


	@command(name="notice", brief="I'll send an official notice regarding the specified issue to the server member on behalf of the server staff.")
	@bot_has_permissions(administrator=True)
	@has_permissions(administrator=True)
	@is_owner()
	async def notice_command(self, ctx, member : Member, *, message):
			notice_embed = Embed(
				title= "Server Notice:",
				colour=(0xa451d8),
				timestamp=datetime.utcnow()
				)
			fields = [("Message:", message, False),
			          ("From server:", ctx.author.guild.name, False)]

			for name, value, inline in fields:
				notice_embed.add_field(name=name, value=value, inline=inline)

			notice_embed.set_thumbnail(url= ctx.guild.icon_url)
			notice_embed.set_footer(text = f'Notice sent by "{ctx.author.name}" to "{member.name}#{member.discriminator}".', icon_url=ctx.author.avatar_url)

			try:
				await member.send(embed = notice_embed)
				await self.log_channel.send(embed=notice_embed)
				await ctx.send("Successfully sent the notice to the member.")

			except Forbidden:
				await ctx.send(f"Unable to send notice. Possibly the mentioned members dms are closed.")

	@notice_command.error
	async def notice_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")

	@command(name="announce", brief="I will make a server announcement through this command.")
	@bot_has_permissions(administrator = True)
	@has_permissions(administrator=True)
	@is_owner()
	async def announce_command(self, ctx, *, message):
		announce_embed = Embed(
			title= "Server Announcement!",
			colour=(0xa451d8),
			timestamp=datetime.utcnow()
			)
		fields = [("Announcement:", message, False)]

		for name, value, inline in fields:
			announce_embed.add_field(name=name, value=value, inline=inline)

		announce_embed.set_thumbnail(url= ctx.guild.icon_url)
		announce_embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Issued by {ctx.author.name}.")

		await ctx.message.delete()
		await self.log_channel.send(embed=announce_embed)
		await ctx.send(embed = announce_embed)

	@announce_command.error
	async def announce_command_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")

	@command(name = "mention everyone", aliases = ["pingeveryone","mention_everyone", "ping_everyone"] ,brief = "If I have the permissions, I will mention everyone in the server through this command.")
	@bot_has_permissions(administrator = True)
	@has_permissions(administrator = True)
	@is_owner()
	async def mention_everyone(self, ctx, *, message: Optional[str] = ""):
		await ctx.message.delete()
		await ctx.send(f"{ctx.message.guild.roles[0]} {message}")

	@mention_everyone.error
	async def mention_everyone_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Command execution failed. Contact SuperNova for more info.")

	@Cog.listener()
	async def on_message(self, message):
		def _check(m):
			return (m.author == message.author
					and len(m.mentions)
					and (datetime.utcnow()-m.created_at).seconds < 60)

		if not message.author.bot:
			if message.channel.id not in self.spam_allowed:
				counter = 0
				with open("./data/spam_detect.txt", "r+") as file:
					for lines in file:
						if lines.strip("\n") == str(message.author.id):
							counter += 1

					file.writelines(f"{str(message.author.id)}\n")
					if counter > 5:
						await message.channel.send(f"{message.author.mention} has been muted for spamming.")
						await self.muted_channel.send(f"{message.author.mention} you have been muted for spamming. If you think this was a mistake, contact the server staff.")
						unmutes = await self.mute_members(message, [message.author], 15, reason="Spam (AUTOMOD)")

						if len(unmutes):
							await sleep(900)
							await self.unmute_members(message.guild, [message.author])	

						await self.warn_members(message, message.author, reason = "Spam (AUTOMOD)")			

			# if len(list(filter(lambda m: _check(m), self.bot.cached_messages))) >= 5:
			# 	await message.channel.send("Don't spam mentions!", delete_after=10)
			# 	unmutes = await self.mute_members(message, [message.author], 60, reason="Mention spam.")

			# 	if len(unmutes):
			# 		await sleep(3600)
			# 		await self.unmute_members(message.guild, [message.author])

			if profanity.contains_profanity(message.content):
				if message.author.id == 424486126351417344:
					pass
				else:
					await message.delete()
					await message.channel.send(f"Do not break the rules {message.author.mention}. You have been warned!")
					await self.warn_members(message, message.author, reason = "Profanity (AUTOMOD)")

			if message.channel.id in self.links_not_allowed and search(self.url_regex, message.content):
				await message.delete()
				await message.channel.send("You can't send links in this channel.", delete_after=10)

			if (message.channel.id in self.images_not_allowed
				and any([hasattr(a, "width") for a in message.attachments])):
				await message.delete()
				await message.channel.send("You can't send images here.", delete_after=10)


def setup(bot):
	bot.add_cog(Mod(bot))
