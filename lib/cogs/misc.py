from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from discord.ext.commands import is_owner
import time 
import asyncio
from discord.ext.menus import MenuPages, ListPageSource
from typing import Optional
from aiohttp import request
from asyncio import sleep
from datetime import datetime, timedelta

from ..db import db

class DefineEmbeds(ListPageSource):
	def __init__(self, ctx):
		self.ctx = ctx

		super().__init__()

class Misc(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("misc")

	@command(name = "reminder", aliases = ["remindme", "remind"])
	@is_owner()
	async def reminder_command(self, ctx, minutes: Optional[int], *, remind_msg):
		if minutes == None:
			await ctx.send(f"{ctx.author.mention} please specify the remind time.")
		else:
			await ctx.send(f"Hai! I'll remind you in `{minutes} minutes` about: `{remind_msg}`")

			reminder_embed = Embed(title = "Reminder!", 
				                   description= f"Nova-kun, you asked me to remind you about:\n **{remind_msg}**",
				                   colour = (0xa451d8),
				                   timestamp=datetime.utcnow()
				                   )

			reminder_embed.set_thumbnail(url = ctx.author.avatar_url)
			await sleep(minutes*60)
			await ctx.send(f"{ctx.author.mention} here's your reminder.", embed = reminder_embed)






	# @command(name = "afk")
	# @is_owner()
	# async def afk_command(self, ctx, message: Optional[str] = f"{ctx.author.name} is currently afk."):
		# with open("./data/afk_msg.txt", "r+") as file:
		# 	file.writelines(f"{message}")

	# 	start_time = time.time()
	# 	await ctx.author.edit(nick = f"~~ [AFK] ~~ {ctx.author.display_name}")
	# 	await ctx.send(f"{ctx.author.mention} I have set your afk to: {message}")


	# @Cog.listener()
	# async def on_message(self, message):
	# 	def _check(m):
	# 		return (m.author == message.author
	# 				and len(m.mentions)
	# 				and (datetime.utcnow()-m.created_at).seconds < 60)

	# 	if not message.author.bot:

	# 		if len(list(filter(lambda m: _check(m), self.bot.cached_messages))) >= 5 and message.author.display_name.startswith("~~ [AFK] ~~ "):
	# 			embed = Embed(description = f"{ctx.message.author} ")





def setup(bot):
	bot.add_cog(Misc(bot))