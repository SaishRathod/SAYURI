from discord import Embed
from discord import Member
from discord.ext.commands import command
from datetime import datetime
from discord.ext.commands import Cog
from typing import Optional
from discord.ext.commands import is_owner

class Info(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command(aliases = ["userinfo", "memberinfo"], brief = "I'll be your personal secret agent and fetch out some top secret intel on the server member.")
	@is_owner()
	async def whois (self, ctx, target: Optional[Member]):
		target = target or ctx.author

		embed = Embed (title = "User Info:",
			           color = (0xa451d8),
			           timestamp = datetime.utcnow())

		embed.set_thumbnail(url = target.avatar_url)

		fields = [("Name:", str(target), True),
		          ("ID:", target.id, True),
		          ("Bot or not:", target.bot, True),
		          ("Created at:", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
		          ("Joined server at:", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
		          ("Status:", str(target.status).title(), True),
		          ("Boosted server:", bool(target.premium_since), True)
		          ]

		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)

		await ctx.send(embed = embed)

	@command(name = "avatar", aliases = ["av",])
	@is_owner()
	async def avatar_command(self, ctx, target: Optional[Member]):
		target = target or ctx.author

		avatar_embed = Embed (title = "Avatar",
			                  color = (0xa451d8))

		avatar_embed.set_image(url = target.avatar_url)
		avatar_embed.set_author(name = f"{target.display_name}#{target.discriminator}", icon_url = target.avatar_url)

		await ctx.send(embed = avatar_embed)

	@command(name = "serverinfo", aliases = ["guildinfo"], brief = "I'll give you some info about the server.")
	@is_owner()
	async def server_info(self, ctx):

		embed = Embed (title = "Server Info:",
			           color = (0xa451d8),
			           timestamp = datetime.utcnow())

		embed.set_thumbnail(url = ctx.guild.icon_url)

		statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

		fields = [("ID:", ctx.guild.id, True),
		          ("Owner:", ctx.guild.owner, True),
		          ("Created on:", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
		          ("Members:", len(ctx.guild.members), True),
		          ("Human Count:", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
		          ("Bot Count:", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
		          ("Statuses:", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
		          ("\u200b", "\u200b", True)
		          ]


		for name, value, inline in fields:
			embed.add_field(name = name, value = value, inline = inline)

		await ctx.send(embed = embed) 
		

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("info")


def setup(bot):
	bot.add_cog(Info(bot))         	



