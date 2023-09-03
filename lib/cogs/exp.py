from datetime import datetime, timedelta
from random import randint
from typing import Optional
from discord import ChannelType
from discord import Member, Embed
from typing import Optional
from discord.ext.commands import Cog
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions
from discord.ext.menus import MenuPages, ListPageSource

from ..db import db


class HelpMenu(ListPageSource):
	def __init__(self, ctx, data):
		self.ctx = ctx

		super().__init__(data, per_page=10)

	async def write_page(self, menu, offset, fields=[]):
		len_data = len(self.entries)

		embed = Embed(title="XP Leaderboard",
					  colour=(0xa451d8))
		embed.set_thumbnail(url=self.ctx.guild.icon_url)
		embed.set_footer(text=f"{offset:,} - {min(len_data, offset+self.per_page-1):,} of {len_data:,} members.")

		for name, value in fields:
			embed.add_field(name=name, value=value, inline=False)

		return embed

	async def format_page(self, menu, entries):
		offset = (menu.current_page*self.per_page) + 1

		fields = []
		table = ("\n".join(f"{idx+offset}. {self.ctx.bot.guild.get_member(entry[0]).name} (XP: {entry[1]} | Level: {entry[2]})"
				for idx, entry in enumerate(entries)))

		fields.append(("Member Ranks:", table))

		return await self.write_page(menu, offset, fields)



class Exp(Cog):
	def __init__(self, bot):
		self.bot = bot

	async def process_xp(self, message):
		xp, lvl, xplock = db.record("SELECT XP, Level, XPLock FROM exp WHERE UserID = ?", message.author.id)

		if datetime.utcnow() > datetime.fromisoformat(xplock):
			await self.add_xp(message, xp, lvl)

	async def add_xp(self, message, xp, lvl):
		xp_to_add = randint(10, 20)
		new_lvl = int(((xp+xp_to_add)//42) ** 0.55)

		db.execute("UPDATE exp SET XP = XP + ?, Level = ?, XPLock = ? WHERE UserID = ?",
				   xp_to_add, new_lvl, (datetime.utcnow()+timedelta(seconds=10)).isoformat(), message.author.id)

		if new_lvl > lvl:
			await message.channel.send(f"Confratzz {message.author.mention}! You are now `lv{new_lvl:,}`!")
			await self.check_lvl_rewards(message, new_lvl)
			await self.check_lvl_rewards(message, new_lvl)

	async def check_lvl_rewards(self, message, lvl):
		if lvl >= 50:                  
			if (new_role := message.guild.get_role(804587003663613952)) not in message.author.roles:
				await message.author.add_roles(new_role)
				#await message.author.remove_roles(message.guild.get_role(653940192780222515))             #<<< Un-comment if you do not want to stack roles.

		elif 40 <= lvl < 50: 
			if (new_role := message.guild.get_role(804590076327231508)) not in message.author.roles:
				await message.author.add_roles(new_role)
				#await message.author.remove_roles(message.guild.get_role(653940254293622794))

		elif 30 <= lvl < 40: 
			if (new_role := message.guild.get_role(804586973850501121)) not in message.author.roles:
				await message.author.add_roles(new_role)
				#await message.author.remove_roles(message.guild.get_role(653940277761015809))

		elif 20 <= lvl < 30:
			if (new_role := message.guild.get_role(804586951445446676)) not in message.author.roles:
				await message.author.add_roles(new_role)
				#await message.author.remove_roles(message.guild.get_role(653940305300815882))

		elif 10 <= lvl < 20: 
			if (new_role := message.guild.get_role(804586870863822879)) not in message.author.roles:
				await message.author.add_roles(new_role)
				#await message.author.remove_roles(message.guild.get_role(653940328453373952))

		elif 5 <= lvl < 9: 
			if (new_role := message.guild.get_role(804586858746871818)) not in message.author.roles:
				await message.author.add_roles(new_role)

	@command(name = "level", aliases = ["lvl", ])
	async def display_level(self, ctx, target: Optional[Member]):
		target = target or ctx.author

		xp, lvl = db.record("SELECT XP, Level FROM exp WHERE UserID = ?", target.id) or (None, None)

		if lvl is not None:
			await ctx.send(f"{target.name} is currently on `lv{lvl:,}` with `{xp:,}XP`.")

		else:
			await ctx.send("A bot does not have a level.")

	@command(name = "rank")
	async def display_rank(self, ctx, target: Optional[Member]):
		target = target or ctx.author

		ids = db.column("SELECT UserID FROM exp ORDER BY XP DESC")

		try:
			await ctx.send(f"{target.name} is `#{ids.index(target.id)+1}/{len(ids)}`.")

		except ValueError:
			await ctx.send("A bot does not have a rank.")

	@command(name = "leaderboard", aliases = ["lb", "xplb"])
	async def display_leaderboard(self, ctx):
		records = db.records("SELECT UserID, XP, Level FROM exp ORDER BY XP DESC")

		menu = MenuPages(source = HelpMenu(ctx, records),
			             delete_message_after=True,
					     timeout=60.0)
		await menu.start(ctx)



	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("exp")

	@Cog.listener()
	async def on_message(self, message):
		if not message.author.bot and message.channel.type != ChannelType.private:
			await self.process_xp(message)


def setup(bot):
	bot.add_cog(Exp(bot))







