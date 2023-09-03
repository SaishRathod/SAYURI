from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands import NotOwner
from discord import Member, Embed
from asyncio import sleep
from discord import Intents
from discord.ext.commands import is_owner
from discord.ext.commands import MissingRequiredArgument
import random
from typing import Optional
import re
import discord
from discord.ext import commands

from ..db import db


class MentionMember(commands.CommandError):
	pass

class Emotes(Cog):
	def __init__(self, bot):
		self.bot = bot


	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("emotes")

	@command(name = "add_operator", aliases = ["addop",])
	@is_owner()
	async def add_opperator_command(self, ctx, member: Member):
		db.execute("INSERT INTO operators VALUES (?, ?)", member.id, f"{member.name}{member.discriminator}")

		await ctx.send("Successfully added the user as an operator.")

		
	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def pat(self, ctx, member: Member, *, message: Optional[str]):
		if member == ctx.author:
			await ctx.send(f"Aww do you want a pat {ctx.author.display_name}?")
		elif not message:
			pats = Embed(
				description = f"{ctx.author.mention} started patting {member.mention}.", color = (0xa451d8))

			pats_gif = [           #30
			"https://media1.tenor.com/images/f330c520a8dfa461130a799faca13c7e/tenor.gif?itemid=13911345",
			"https://media1.tenor.com/images/6ee188a109975a825f53e0dfa56d497d/tenor.gif?itemid=17747839",
			"https://media1.tenor.com/images/da8f0e8dd1a7f7db5298bda9cc648a9a/tenor.gif?itemid=12018819",
			"https://media1.tenor.com/images/daa885ec8a9cfa4107eb966df05ba260/tenor.gif?itemid=13792462",
			"https://media1.tenor.com/images/c0bcaeaa785a6bdf1fae82ecac65d0cc/tenor.gif?itemid=7453915",
			"https://media1.tenor.com/images/6151c42c94df654b1c7de2fdebaa6bd1/tenor.gif?itemid=16456868",
			"https://media1.tenor.com/images/54722063c802bac30d928db3bf3cc3b4/tenor.gif?itemid=8841561",
			"https://media1.tenor.com/images/0d2fb6ad9a6d71c3a018c0b37ffca50b/tenor.gif?itemid=16121044",
			"https://media1.tenor.com/images/5466adf348239fba04c838639525c28a/tenor.gif?itemid=13284057",
			"https://media1.tenor.com/images/c0c1c5d15f8ad65a9f0aaf6c91a3811e/tenor.gif?itemid=13410974",
			"https://media1.tenor.com/images/01a97fee428982b325269207ca22866b/tenor.gif?itemid=16085328",
			"https://media1.tenor.com/images/8c1f6874db27c8227755a08b2b07740b/tenor.gif?itemid=10789367",
			"https://media1.tenor.com/images/f48ffb8cf033d1aefe4693045aedad5a/tenor.gif?itemid=4086973",
			"https://media1.tenor.com/images/13f385a3442ac5b513a0fa8e8d805567/tenor.gif?itemid=13857199",
			"https://media1.tenor.com/images/61187dd8c7985c443bf9cd39bc310c02/tenor.gif?itemid=12018805",
			"https://media1.tenor.com/images/28f4f29de42f03f66fb17c5621e7bedf/tenor.gif?itemid=8659513",
			"https://media1.tenor.com/images/078272218e0044768b52c50ffd78de0a/tenor.gif?itemid=20183996",
			"https://media1.tenor.com/images/fb3e0b0f18188450bfded4a585de2b90/tenor.gif?itemid=8208759",
			"https://media1.tenor.com/images/e46884c4930c77aec1ccf954efcc5292/tenor.gif?itemid=16236557",
			"https://media1.tenor.com/images/2b3ddd79058842ccb9c1fc6acea0bcaa/tenor.gif?itemid=16243971", 
			"https://media1.tenor.com/images/291ea37382e1d6cd33349c50a398b6b9/tenor.gif?itemid=10204936", 
			"https://media1.tenor.com/images/46bab773fdf4c340b59b89655abcda79/tenor.gif?itemid=18776498",
			"https://media1.tenor.com/images/37b0ba8252f8698d23c83d889768540b/tenor.gif?itemid=19580650",
			"https://media1.tenor.com/images/c2232aec426d8b5e85e026cbca410463/tenor.gif?itemid=11648944",
			"https://media1.tenor.com/images/d3c117054fb924d66c75169ff158c811/tenor.gif?itemid=15471762",
			"https://media1.tenor.com/images/0a35a0cc82d3b613086e0f420a94c2ad/tenor.gif?itemid=15779012",
			"https://media1.tenor.com/images/0444a1b1e7af31dde95dc67c44c18ce7/tenor.gif?itemid=14368378",
			"https://cdn.weeb.sh/images/r1goyytPZ.gif",
			"https://cdn.weeb.sh/images/SJLaWWRSG.gif",
			"https://cdn.weeb.sh/images/SJudB96_f.gif",
			]
			pats.set_image(url = random.choice(pats_gif))
			await ctx.send(embed = pats)
		else:
			pats = Embed(
				description = message, color = (0xa451d8))

			pats_gif = [           #30
			"https://media1.tenor.com/images/f330c520a8dfa461130a799faca13c7e/tenor.gif?itemid=13911345",
			"https://media1.tenor.com/images/6ee188a109975a825f53e0dfa56d497d/tenor.gif?itemid=17747839",
			"https://media1.tenor.com/images/da8f0e8dd1a7f7db5298bda9cc648a9a/tenor.gif?itemid=12018819",
			"https://media1.tenor.com/images/daa885ec8a9cfa4107eb966df05ba260/tenor.gif?itemid=13792462",
			"https://media1.tenor.com/images/c0bcaeaa785a6bdf1fae82ecac65d0cc/tenor.gif?itemid=7453915",
			"https://media1.tenor.com/images/6151c42c94df654b1c7de2fdebaa6bd1/tenor.gif?itemid=16456868",
			"https://media1.tenor.com/images/54722063c802bac30d928db3bf3cc3b4/tenor.gif?itemid=8841561",
			"https://media1.tenor.com/images/0d2fb6ad9a6d71c3a018c0b37ffca50b/tenor.gif?itemid=16121044",
			"https://media1.tenor.com/images/5466adf348239fba04c838639525c28a/tenor.gif?itemid=13284057",
			"https://media1.tenor.com/images/c0c1c5d15f8ad65a9f0aaf6c91a3811e/tenor.gif?itemid=13410974",
			"https://media1.tenor.com/images/01a97fee428982b325269207ca22866b/tenor.gif?itemid=16085328",
			"https://media1.tenor.com/images/8c1f6874db27c8227755a08b2b07740b/tenor.gif?itemid=10789367",
			"https://media1.tenor.com/images/f48ffb8cf033d1aefe4693045aedad5a/tenor.gif?itemid=4086973",
			"https://media1.tenor.com/images/13f385a3442ac5b513a0fa8e8d805567/tenor.gif?itemid=13857199",
			"https://media1.tenor.com/images/61187dd8c7985c443bf9cd39bc310c02/tenor.gif?itemid=12018805",
			"https://media1.tenor.com/images/28f4f29de42f03f66fb17c5621e7bedf/tenor.gif?itemid=8659513",
			"https://media1.tenor.com/images/078272218e0044768b52c50ffd78de0a/tenor.gif?itemid=20183996",
			"https://media1.tenor.com/images/fb3e0b0f18188450bfded4a585de2b90/tenor.gif?itemid=8208759",
			"https://media1.tenor.com/images/e46884c4930c77aec1ccf954efcc5292/tenor.gif?itemid=16236557",
			"https://media1.tenor.com/images/2b3ddd79058842ccb9c1fc6acea0bcaa/tenor.gif?itemid=16243971", 
			"https://media1.tenor.com/images/291ea37382e1d6cd33349c50a398b6b9/tenor.gif?itemid=10204936", 
			"https://media1.tenor.com/images/46bab773fdf4c340b59b89655abcda79/tenor.gif?itemid=18776498",
			"https://media1.tenor.com/images/37b0ba8252f8698d23c83d889768540b/tenor.gif?itemid=19580650",
			"https://media1.tenor.com/images/c2232aec426d8b5e85e026cbca410463/tenor.gif?itemid=11648944",
			"https://media1.tenor.com/images/d3c117054fb924d66c75169ff158c811/tenor.gif?itemid=15471762",
			"https://media1.tenor.com/images/0a35a0cc82d3b613086e0f420a94c2ad/tenor.gif?itemid=15779012",
			"https://media1.tenor.com/images/0444a1b1e7af31dde95dc67c44c18ce7/tenor.gif?itemid=14368378",
			"https://cdn.weeb.sh/images/r1goyytPZ.gif",
			"https://cdn.weeb.sh/images/SJLaWWRSG.gif",
			"https://cdn.weeb.sh/images/SJudB96_f.gif",
			]
			pats.set_image(url = random.choice(pats_gif))
			await ctx.send(embed = pats)			

	@pat.error
	async def pat_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.", aliases = ["poke",])
	# @is_owner()
	async def boop(self, ctx, member: Member, *, message: Optional[str]):
		if member == ctx.author:
			await ctx.send(f"{ctx.author.display_name} wants someone to boop them?")
		elif not message:
			boop = Embed(
				description = f"{ctx.author.mention} started booping {member.mention}.", color = (0xa451d8))
			boops_gif = [
			"https://media1.tenor.com/images/567ba9e70f306c5ce6432377840437d3/tenor.gif?itemid=14746195",
			"https://media1.tenor.com/images/0da232de2ee45e1464bf1d5916869a39/tenor.gif?itemid=16935454",
			"https://media1.tenor.com/images/cbf38a2e97a348a621207c967a77628a/tenor.gif?itemid=6287077",
			"https://media1.tenor.com/images/fde75886df37020bc37d7ba44c1e29ee/tenor.gif?itemid=15255810",
			"https://media1.tenor.com/images/a0f0c6b3ef95bb2ff530a92d6c516cbd/tenor.gif?itemid=14452125",
			"https://media1.tenor.com/images/dbde71d42e747010b980422b88e77f9b/tenor.gif?itemid=16935420",
			"https://media1.tenor.com/images/1caed87934a37ac144e9876c9fe8d2a6/tenor.gif?itemid=15643263",
			"https://cdn.weeb.sh/images/HkxwlkKPb.gif",
			"https://cdn.weeb.sh/images/SydLxJFwW.gif",
			"https://cdn.weeb.sh/images/r1ALxJKwW.gif",
			"https://cdn.weeb.sh/images/rJzUe1FwZ.gif",
			"https://cdn.weeb.sh/images/rkB8eJYPZ.gif",
			"https://cdn.weeb.sh/images/rktSlkKvb.gif",
			"https://cdn.weeb.sh/images/rkaUe1YPb.gif",
			"https://cdn.weeb.sh/images/rkeaUeJKD-.gif",
			"https://cdn.weeb.sh/images/B14SJlTQG.gif",
			"https://cdn.weeb.sh/images/HJZpLxkKDb.gif",
			"https://cdn.weeb.sh/images/SyQzRaFFb.gif",
			"https://cdn.weeb.sh/images/rJ0hlsnR-.gif",
			"https://cdn.weeb.sh/images/BkcSekKwb.gif",
			]
			boop.set_image(url = random.choice(boops_gif))
			await ctx.send(embed = boop)	
		else:
			boop = Embed(description = message, color = (0xa451d8))
			boops_gif = [
			"https://media1.tenor.com/images/567ba9e70f306c5ce6432377840437d3/tenor.gif?itemid=14746195",
			"https://media1.tenor.com/images/0da232de2ee45e1464bf1d5916869a39/tenor.gif?itemid=16935454",
			"https://media1.tenor.com/images/cbf38a2e97a348a621207c967a77628a/tenor.gif?itemid=6287077",
			"https://media1.tenor.com/images/fde75886df37020bc37d7ba44c1e29ee/tenor.gif?itemid=15255810",
			"https://media1.tenor.com/images/a0f0c6b3ef95bb2ff530a92d6c516cbd/tenor.gif?itemid=14452125",
			"https://media1.tenor.com/images/dbde71d42e747010b980422b88e77f9b/tenor.gif?itemid=16935420",
			"https://media1.tenor.com/images/1caed87934a37ac144e9876c9fe8d2a6/tenor.gif?itemid=15643263",
			"https://cdn.weeb.sh/images/HkxwlkKPb.gif",
			"https://cdn.weeb.sh/images/SydLxJFwW.gif",
			"https://cdn.weeb.sh/images/r1ALxJKwW.gif",
			"https://cdn.weeb.sh/images/rJzUe1FwZ.gif",
			"https://cdn.weeb.sh/images/rkB8eJYPZ.gif",
			"https://cdn.weeb.sh/images/rktSlkKvb.gif",
			"https://cdn.weeb.sh/images/rkaUe1YPb.gif",
			"https://cdn.weeb.sh/images/rkeaUeJKD-.gif",
			"https://cdn.weeb.sh/images/B14SJlTQG.gif",
			"https://cdn.weeb.sh/images/HJZpLxkKDb.gif",
			"https://cdn.weeb.sh/images/SyQzRaFFb.gif",
			"https://cdn.weeb.sh/images/rJ0hlsnR-.gif",
			"https://cdn.weeb.sh/images/BkcSekKwb.gif",
			]
			boop.set_image(url = random.choice(boops_gif))
			await ctx.send(embed = boop)	

	@boop.error
	async def boop_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def hug(self, ctx, member: Member, *, message: Optional[str]):
		if member == ctx.author:
			await ctx.send(f"{ctx.author.display_name} wants a hug....")		
		elif not message:
			if ctx.author.id == 424486126351417344 and member == ctx.me:
				hug = Embed(
					description = f"{ctx.author.mention} hugs {member.mention}. Thank you Nova-kun!",
					color = (0xa451d8)
				)

				hug_gif = [               #30
				"https://media1.tenor.com/images/daffa3b7992a08767168614178cce7d6/tenor.gif?itemid=15249774",
				"https://media1.tenor.com/images/1d94b18b89f600cbb420cce85558b493/tenor.gif?itemid=15942846",
				"https://media1.tenor.com/images/bb9c0c56769afa3b58b9efe5c7bcaafb/tenor.gif?itemid=16831471",
				"https://media1.tenor.com/images/b4ba20e6cb49d8f8bae81d86e45e4dcc/tenor.gif?itemid=5634582",
				"https://media1.tenor.com/images/42922e87b3ec288b11f59ba7f3cc6393/tenor.gif?itemid=5634630",
				"https://media1.tenor.com/images/16f4ef8659534c88264670265e2a1626/tenor.gif?itemid=14903944",
				"https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
				"https://media1.tenor.com/images/b77fd0cfd95f89f967be0a5ebb3b6c6a/tenor.gif?itemid=7864716",
				"https://media1.tenor.com/images/228cc8397577141822195070c88f6083/tenor.gif?itemid=4977890",
				"https://media1.tenor.com/images/c1058ebe89313d50dfc878d38630036b/tenor.gif?itemid=13976210",
				"https://media1.tenor.com/images/8a4bee08487ba219fdadeee531e67c97/tenor.gif?itemid=17770800",
				"https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/tenor.gif?itemid=10522729",
				"https://media1.tenor.com/images/b62f047f8ed11b832cb6c0d8ec30687b/tenor.gif?itemid=12668480",
				"https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498",
				"https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587",
				"https://cdn.weeb.sh/images/BJF5_uXvZ.gif",
				"https://cdn.weeb.sh/images/SJfEks3Rb.gif",
				"https://cdn.weeb.sh/images/BkBs2uk_b.gif",
				"https://cdn.weeb.sh/images/HJU2OdmwW.gif",
				"https://cdn.weeb.sh/images/Sk-xxs3C-.gif",
				"https://cdn.weeb.sh/images/r1kC_dQPW.gif",
				"https://cdn.weeb.sh/images/BJx2l0ttW.gif",
				"https://cdn.weeb.sh/images/HkRwnuyuW.gif",
				"https://cdn.weeb.sh/images/r1v2_uXP-.gif",
				"https://cdn.weeb.sh/images/SywetdQvZ.gif",
				]
				hug.set_image(url = random.choice(hug_gif))
				await ctx.send(embed = hug)

			else:
				hug = Embed(
					description = f"{ctx.author.mention} hugs {member.mention}.",
					color = (0xa451d8)
				)

				hug_gif = [               #30
				"https://media1.tenor.com/images/daffa3b7992a08767168614178cce7d6/tenor.gif?itemid=15249774",
				"https://media1.tenor.com/images/1d94b18b89f600cbb420cce85558b493/tenor.gif?itemid=15942846",
				"https://media1.tenor.com/images/bb9c0c56769afa3b58b9efe5c7bcaafb/tenor.gif?itemid=16831471",
				"https://media1.tenor.com/images/b4ba20e6cb49d8f8bae81d86e45e4dcc/tenor.gif?itemid=5634582",
				"https://media1.tenor.com/images/42922e87b3ec288b11f59ba7f3cc6393/tenor.gif?itemid=5634630",
				"https://media1.tenor.com/images/16f4ef8659534c88264670265e2a1626/tenor.gif?itemid=14903944",
				"https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
				"https://media1.tenor.com/images/b77fd0cfd95f89f967be0a5ebb3b6c6a/tenor.gif?itemid=7864716",
				"https://media1.tenor.com/images/228cc8397577141822195070c88f6083/tenor.gif?itemid=4977890",
				"https://media1.tenor.com/images/c1058ebe89313d50dfc878d38630036b/tenor.gif?itemid=13976210",
				"https://media1.tenor.com/images/8a4bee08487ba219fdadeee531e67c97/tenor.gif?itemid=17770800",
				"https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/tenor.gif?itemid=10522729",
				"https://media1.tenor.com/images/b62f047f8ed11b832cb6c0d8ec30687b/tenor.gif?itemid=12668480",
				"https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498",
				"https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587",
				"https://cdn.weeb.sh/images/BJF5_uXvZ.gif",
				"https://cdn.weeb.sh/images/SJfEks3Rb.gif",
				"https://cdn.weeb.sh/images/BkBs2uk_b.gif",
				"https://cdn.weeb.sh/images/HJU2OdmwW.gif",
				"https://cdn.weeb.sh/images/Sk-xxs3C-.gif",
				"https://cdn.weeb.sh/images/r1kC_dQPW.gif",
				"https://cdn.weeb.sh/images/BJx2l0ttW.gif",
				"https://cdn.weeb.sh/images/HkRwnuyuW.gif",
				"https://cdn.weeb.sh/images/r1v2_uXP-.gif",
				"https://cdn.weeb.sh/images/SywetdQvZ.gif",
				]
				hug.set_image(url = random.choice(hug_gif))
				await ctx.send(embed = hug)	

		else:
			hug = Embed(
				description = message,
				color = (0xa451d8)
			)

			hug_gif = [               #30
			"https://media1.tenor.com/images/daffa3b7992a08767168614178cce7d6/tenor.gif?itemid=15249774",
			"https://media1.tenor.com/images/1d94b18b89f600cbb420cce85558b493/tenor.gif?itemid=15942846",
			"https://media1.tenor.com/images/bb9c0c56769afa3b58b9efe5c7bcaafb/tenor.gif?itemid=16831471",
			"https://media1.tenor.com/images/b4ba20e6cb49d8f8bae81d86e45e4dcc/tenor.gif?itemid=5634582",
			"https://media1.tenor.com/images/42922e87b3ec288b11f59ba7f3cc6393/tenor.gif?itemid=5634630",
			"https://media1.tenor.com/images/16f4ef8659534c88264670265e2a1626/tenor.gif?itemid=14903944",
			"https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
			"https://media1.tenor.com/images/b77fd0cfd95f89f967be0a5ebb3b6c6a/tenor.gif?itemid=7864716",
			"https://media1.tenor.com/images/228cc8397577141822195070c88f6083/tenor.gif?itemid=4977890",
			"https://media1.tenor.com/images/c1058ebe89313d50dfc878d38630036b/tenor.gif?itemid=13976210",
			"https://media1.tenor.com/images/8a4bee08487ba219fdadeee531e67c97/tenor.gif?itemid=17770800",
			"https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/tenor.gif?itemid=10522729",
			"https://media1.tenor.com/images/b62f047f8ed11b832cb6c0d8ec30687b/tenor.gif?itemid=12668480",
			"https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498",
			"https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587",
			"https://cdn.weeb.sh/images/BJF5_uXvZ.gif",
			"https://cdn.weeb.sh/images/SJfEks3Rb.gif",
			"https://cdn.weeb.sh/images/BkBs2uk_b.gif",
			"https://cdn.weeb.sh/images/HJU2OdmwW.gif",
			"https://cdn.weeb.sh/images/Sk-xxs3C-.gif",
			"https://cdn.weeb.sh/images/r1kC_dQPW.gif",
			"https://cdn.weeb.sh/images/BJx2l0ttW.gif",
			"https://cdn.weeb.sh/images/HkRwnuyuW.gif",
			"https://cdn.weeb.sh/images/r1v2_uXP-.gif",
			"https://cdn.weeb.sh/images/SywetdQvZ.gif",
			]
			hug.set_image(url = random.choice(hug_gif))
			await ctx.send(embed = hug)

	  
	@hug.error
	async def hug_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")


	@command(brief = "Action/Emote command.")
	@is_owner()
	async def cuddle(self, ctx, member: Member, *, message: Optional[str]):
		if member == ctx.author:
			await ctx.send(f"Do you wanna cuddle {ctx.author.mention}?")
		elif not message:
			if member == ctx.me:
				cuddles = Embed(
					description = f"{ctx.author.mention} cuddles {member.mention}. I love cuddling with you Nova-kun.",
				    color = (0xa451d8)
				)
				cuddles_gif = [   #25
				"https://media1.tenor.com/images/1186825907f3761c1f02579a5e191b02/tenor.gif?itemid=4769751",
				"https://media1.tenor.com/images/94989f6312726739893d41231942bb1b/tenor.gif?itemid=14106856",
				"https://media1.tenor.com/images/f5df55943b64922b6b16aa63d43243a6/tenor.gif?itemid=9375012",
				"https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075",
				"https://media1.tenor.com/images/9fcdeda4151062b6191d35eb565d676a/tenor.gif?itemid=17956092",
				"https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif?itemid=5044460",
				"https://media1.tenor.com/images/85dcef131af84b515106955e142df54e/tenor.gif?itemid=13857541",
				"https://media1.tenor.com/images/aa04a0093e2ef93922d3d88e12b70561/tenor.gif?itemid=12887276",
				"https://media1.tenor.com/images/7ece0d6e9306763eeea5e0c5284a3528/tenor.gif?itemid=14106855",
				"https://media1.tenor.com/images/205cde7485168c9d7aac25106a80eece/tenor.gif?itemid=14844150",
				"https://cdn.weeb.sh/images/r17lwymiZ.gif",
				"https://cdn.weeb.sh/images/BkTe8U7v-.gif",
				"https://cdn.weeb.sh/images/BJkABImvb.gif",
				"https://cdn.weeb.sh/images/SJceIU7wZ.gif",
				"https://cdn.weeb.sh/images/S1T91Att-.gif",
				"https://cdn.weeb.sh/images/H1SfI8XwW.gif",
				"https://cdn.weeb.sh/images/HkZDkeamf.gif",
				"https://cdn.weeb.sh/images/BywGX8caZ.gif",
				"https://cdn.weeb.sh/images/r1Q0HImPZ.gif",
				"https://cdn.weeb.sh/images/rJ6zAkc1f.gif",
				"https://cdn.weeb.sh/images/BkTe8U7v-.gif",
				"https://cdn.weeb.sh/images/B1Qb88XvW.gif",
				"https://cdn.weeb.sh/images/rJlMU87vb.gif",
				"https://cdn.weeb.sh/images/r1A77CZbz.gif",
				"https://cdn.weeb.sh/images/SJLkLImPb.gif",
				]
				cuddles.set_image(url = random.choice(cuddles_gif))
				await ctx.send(embed = cuddles)
			else:
				await sleep(1)
				await ctx.message.delete()
				await ctx.send("**NO**", delete_after = 5)
		else:
			cuddles = Embed(
				description = message,
			    color = (0xa451d8)
			)
			cuddles_gif = [   #25
			"https://media1.tenor.com/images/1186825907f3761c1f02579a5e191b02/tenor.gif?itemid=4769751",
			"https://media1.tenor.com/images/94989f6312726739893d41231942bb1b/tenor.gif?itemid=14106856",
			"https://media1.tenor.com/images/f5df55943b64922b6b16aa63d43243a6/tenor.gif?itemid=9375012",
			"https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075",
			"https://media1.tenor.com/images/9fcdeda4151062b6191d35eb565d676a/tenor.gif?itemid=17956092",
			"https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif?itemid=5044460",
			"https://media1.tenor.com/images/85dcef131af84b515106955e142df54e/tenor.gif?itemid=13857541",
			"https://media1.tenor.com/images/aa04a0093e2ef93922d3d88e12b70561/tenor.gif?itemid=12887276",
			"https://media1.tenor.com/images/7ece0d6e9306763eeea5e0c5284a3528/tenor.gif?itemid=14106855",
			"https://media1.tenor.com/images/205cde7485168c9d7aac25106a80eece/tenor.gif?itemid=14844150",
			"https://cdn.weeb.sh/images/r17lwymiZ.gif",
			"https://cdn.weeb.sh/images/BkTe8U7v-.gif",
			"https://cdn.weeb.sh/images/BJkABImvb.gif",
			"https://cdn.weeb.sh/images/SJceIU7wZ.gif",
			"https://cdn.weeb.sh/images/S1T91Att-.gif",
			"https://cdn.weeb.sh/images/H1SfI8XwW.gif",
			"https://cdn.weeb.sh/images/HkZDkeamf.gif",
			"https://cdn.weeb.sh/images/BywGX8caZ.gif",
			"https://cdn.weeb.sh/images/r1Q0HImPZ.gif",
			"https://cdn.weeb.sh/images/rJ6zAkc1f.gif",
			"https://cdn.weeb.sh/images/BkTe8U7v-.gif",
			"https://cdn.weeb.sh/images/B1Qb88XvW.gif",
			"https://cdn.weeb.sh/images/rJlMU87vb.gif",
			"https://cdn.weeb.sh/images/r1A77CZbz.gif",
			"https://cdn.weeb.sh/images/SJLkLImPb.gif",
			]
			cuddles.set_image(url = random.choice(cuddles_gif))
			await ctx.send(embed = cuddles)

	@cuddle.error
	async def cuddle_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")


	@command(brief = "Action/Emote command.")
	@is_owner()
	async def kiss(self, ctx, member: Member, *, message: Optional[str]):
		if member == ctx.author:
			await ctx.send(f"My sources say kissing yourself is not practically possible {ctx.author.display_name}.")
		elif not message:
			if member == ctx.me:
				kiss = Embed(
					description = f"{ctx.author.mention} kisses {member.mention}. I l-love you Nova-kun!",
					color = (0xa451d8)
				)
				kiss_gif = [                      #40
				"https://media1.tenor.com/images/503bb007a3c84b569153dcfaaf9df46a/tenor.gif?itemid=17382412",
				"https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865",
				"https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515",
				"https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/tenor.gif?itemid=9838409",
				"https://media1.tenor.com/images/e76e640bbbd4161345f551bb42e6eb13/tenor.gif?itemid=4829336",
				"https://media1.tenor.com/images/a1f7d43752168b3c1dbdfb925bda8a33/tenor.gif?itemid=10356314",
				"https://media1.tenor.com/images/1306732d3351afe642c9a7f6d46f548e/tenor.gif?itemid=6155670",
				"https://media1.tenor.com/images/b8d0152fbe9ecc061f9ad7ff74533396/tenor.gif?itemid=5372258",
				"https://media1.tenor.com/images/d0cd64030f383d56e7edc54a484d4b8d/tenor.gif?itemid=17382422",
				"https://media1.tenor.com/images/ba1841e4aeb5328e41530d3289616f46/tenor.gif?itemid=14240425",
				"https://media1.tenor.com/images/4b5d5afd747fe053ed79317628aac106/tenor.gif?itemid=5649376",
				"https://media1.tenor.com/images/9fac3eab2f619789b88fdf9aa5ca7b8f/tenor.gif?itemid=12925177",
				"https://media1.tenor.com/images/230e9fd40cd15e3f27fc891bac04248e/tenor.gif?itemid=14751754",
				"https://media1.tenor.com/images/ef4a0bcb6e42189dc12ee55e0d479c54/tenor.gif?itemid=12143127",
				"https://media1.tenor.com/images/f34f73decaef049f9354b27984dfb09c/tenor.gif?itemid=14958166",
				"https://media1.tenor.com/images/558f63303a303abfdddaa71dc7b3d6ae/tenor.gif?itemid=12879850",
				"https://media1.tenor.com/images/32d4f0642ebb373e3eb072b2b91e6064/tenor.gif?itemid=15150255",
				"https://media1.tenor.com/images/d7bddc2032a53da99f9a3e5bfadf3cf2/tenor.gif?itemid=17708192",
				"https://media1.tenor.com/images/896519dafbd82b9b924b575e3076708d/tenor.gif?itemid=8811697",
				"https://media1.tenor.com/images/57e94f8aecfa6a7ee7e00b7ceb6d9df1/tenor.gif?itemid=18039109",
				"https://media1.tenor.com/images/d1a11805180742c70339a6bfd7745f8d/tenor.gif?itemid=4883557",
				"https://media1.tenor.com/images/d93c9a9c201ec1fe3c8011718b18a83c/tenor.gif?itemid=16317577",
				"https://media1.tenor.com/images/ad514e809adc14f0b7722a324c2eb36e/tenor.gif?itemid=14375355",
				"https://media1.tenor.com/images/3deb7cd6c872b3774485ae2b3b2f657c/tenor.gif?itemid=13907866",
				"https://media1.tenor.com/images/632a3db90c6ecd87f1242605f92120c7/tenor.gif?itemid=5608449",
				"https://media1.tenor.com/images/f34f73decaef049f9354b27984dfb09c/tenor.gif?itemid=14958166",
				"https://media1.tenor.com/images/9b4892906aaea841c0b6cabd84f29f07/tenor.gif?itemid=13890623",
				"https://media1.tenor.com/images/44fc02255c87e371689e33d084c6a58d/tenor.gif?itemid=12857501",
				"https://media1.tenor.com/images/87647ec4c010442874d7ce7dd61d5e49/tenor.gif?itemid=20301892",
				"https://media1.tenor.com/images/36f11bef515506ccfa2b5cef01d6cb8b/tenor.gif?itemid=17076575",
				"https://media1.tenor.com/images/e6ef659224d7fb9c69c0f675146e8c93/tenor.gif?itemid=17845598",
				"https://cdn.weeb.sh/images/H1a42auvb.gif",
				"https://cdn.weeb.sh/images/BkLQnT_PZ.gif",
				"https://cdn.weeb.sh/images/HJlWhpdw-.gif",
				"https://cdn.weeb.sh/images/HkZyXs3A-.gif",
				"https://cdn.weeb.sh/images/BkUJNec1M.gif",
				"https://cdn.weeb.sh/images/BydoCy9yG.gif",
				"https://cdn.weeb.sh/images/Sksk4l51z.gif",
				"https://cdn.weeb.sh/images/ByoCoT_vW.gif",
				"https://cdn.weeb.sh/images/SydfnauPb.gif",
				]
				kiss.set_image(url = random.choice(kiss_gif))
				await ctx.send(embed = kiss)
			else:
				await sleep(1)
				await ctx.message.delete()
				await ctx.send("**NO**", delete_after = 5)

		else:
			kiss = Embed(
				description = message,
				color = (0xa451d8)
			)
			kiss_gif = [                      #40
			"https://media1.tenor.com/images/503bb007a3c84b569153dcfaaf9df46a/tenor.gif?itemid=17382412",
			"https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865",
			"https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515",
			"https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/tenor.gif?itemid=9838409",
			"https://media1.tenor.com/images/e76e640bbbd4161345f551bb42e6eb13/tenor.gif?itemid=4829336",
			"https://media1.tenor.com/images/a1f7d43752168b3c1dbdfb925bda8a33/tenor.gif?itemid=10356314",
			"https://media1.tenor.com/images/1306732d3351afe642c9a7f6d46f548e/tenor.gif?itemid=6155670",
			"https://media1.tenor.com/images/b8d0152fbe9ecc061f9ad7ff74533396/tenor.gif?itemid=5372258",
			"https://media1.tenor.com/images/d0cd64030f383d56e7edc54a484d4b8d/tenor.gif?itemid=17382422",
			"https://media1.tenor.com/images/ba1841e4aeb5328e41530d3289616f46/tenor.gif?itemid=14240425",
			"https://media1.tenor.com/images/4b5d5afd747fe053ed79317628aac106/tenor.gif?itemid=5649376",
			"https://media1.tenor.com/images/9fac3eab2f619789b88fdf9aa5ca7b8f/tenor.gif?itemid=12925177",
			"https://media1.tenor.com/images/230e9fd40cd15e3f27fc891bac04248e/tenor.gif?itemid=14751754",
			"https://media1.tenor.com/images/ef4a0bcb6e42189dc12ee55e0d479c54/tenor.gif?itemid=12143127",
			"https://media1.tenor.com/images/f34f73decaef049f9354b27984dfb09c/tenor.gif?itemid=14958166",
			"https://media1.tenor.com/images/558f63303a303abfdddaa71dc7b3d6ae/tenor.gif?itemid=12879850",
			"https://media1.tenor.com/images/32d4f0642ebb373e3eb072b2b91e6064/tenor.gif?itemid=15150255",
			"https://media1.tenor.com/images/d7bddc2032a53da99f9a3e5bfadf3cf2/tenor.gif?itemid=17708192",
			"https://media1.tenor.com/images/896519dafbd82b9b924b575e3076708d/tenor.gif?itemid=8811697",
			"https://media1.tenor.com/images/57e94f8aecfa6a7ee7e00b7ceb6d9df1/tenor.gif?itemid=18039109",
			"https://media1.tenor.com/images/d1a11805180742c70339a6bfd7745f8d/tenor.gif?itemid=4883557",
			"https://media1.tenor.com/images/d93c9a9c201ec1fe3c8011718b18a83c/tenor.gif?itemid=16317577",
			"https://media1.tenor.com/images/ad514e809adc14f0b7722a324c2eb36e/tenor.gif?itemid=14375355",
			"https://media1.tenor.com/images/3deb7cd6c872b3774485ae2b3b2f657c/tenor.gif?itemid=13907866",
			"https://media1.tenor.com/images/632a3db90c6ecd87f1242605f92120c7/tenor.gif?itemid=5608449",
			"https://media1.tenor.com/images/f34f73decaef049f9354b27984dfb09c/tenor.gif?itemid=14958166",
			"https://media1.tenor.com/images/9b4892906aaea841c0b6cabd84f29f07/tenor.gif?itemid=13890623",
			"https://media1.tenor.com/images/44fc02255c87e371689e33d084c6a58d/tenor.gif?itemid=12857501",
			"https://media1.tenor.com/images/87647ec4c010442874d7ce7dd61d5e49/tenor.gif?itemid=20301892",
			"https://media1.tenor.com/images/36f11bef515506ccfa2b5cef01d6cb8b/tenor.gif?itemid=17076575",
			"https://media1.tenor.com/images/e6ef659224d7fb9c69c0f675146e8c93/tenor.gif?itemid=17845598",
			"https://cdn.weeb.sh/images/H1a42auvb.gif",
			"https://cdn.weeb.sh/images/BkLQnT_PZ.gif",
			"https://cdn.weeb.sh/images/HJlWhpdw-.gif",
			"https://cdn.weeb.sh/images/HkZyXs3A-.gif",
			"https://cdn.weeb.sh/images/BkUJNec1M.gif",
			"https://cdn.weeb.sh/images/BydoCy9yG.gif",
			"https://cdn.weeb.sh/images/Sksk4l51z.gif",
			"https://cdn.weeb.sh/images/ByoCoT_vW.gif",
			"https://cdn.weeb.sh/images/SydfnauPb.gif",
			]
			kiss.set_image(url = random.choice(kiss_gif))
			await ctx.send(embed = kiss)

	@kiss.error
	async def kiss_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def slap(self, ctx, member: Member, *, message:Optional[str]):
		if member == ctx.author:
			await ctx.send(f"Stop slapping yourself {ctx.author.display_name}!")
		elif not message:
			slap = Embed(
				description = f"{ctx.author.mention} slaps {member.mention}.",
				color = (0xa451d8))
			slap_gif = [            #30
			"https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
			"https://media1.tenor.com/images/e846e892dc50a12bd323ff79690f2050/tenor.gif?itemid=19594595",
			"https://media1.tenor.com/images/1125596130202a28802dd2fe20804426/tenor.gif?itemid=17897244",
			"https://media1.tenor.com/images/74db8b0b64e8d539aebebfbb2094ae84/tenor.gif?itemid=15144612",
			"https://media1.tenor.com/images/53d180f129f51575a46b6d3f0f5eeeea/tenor.gif?itemid=5373994",
			"https://media1.tenor.com/images/7437caf9fb0bea289a5bb163b90163c7/tenor.gif?itemid=13595529",
			"https://media1.tenor.com/images/b221fb3f50f0e15b3ace6a2b87ad0ffa/tenor.gif?itemid=8576304",
			"https://media1.tenor.com/images/07b4516d50406b4a320269d514876170/tenor.gif?itemid=17897216",
			"https://media1.tenor.com/images/f7f0d538542373e7e5366b281d3772e7/tenor.gif?itemid=17303228",
			"https://media1.tenor.com/images/6e27186637897c41ac8fcc407521ab11/tenor.gif?itemid=16412212",
			"https://media1.tenor.com/images/ce295550c5436b7b61edac89b3a49b07/tenor.gif?itemid=16335313",
			"https://media1.tenor.com/images/0892a52155ac70d401126ede4d46ed5e/tenor.gif?itemid=12946466",
			"https://media1.tenor.com/images/55be806f33223b4cf185ccfbadca6a0a/tenor.gif?itemid=20504868",
			"https://media1.tenor.com/images/b3348f0f97514f50b9449d63fc343fe3/tenor.gif?itemid=8065158",
			"https://media1.tenor.com/images/cd9559dc9ffc589137b877028bf93176/tenor.gif?itemid=12803383",
			"https://media1.tenor.com/images/6138bdbf998fde7638b8362499ac5427/tenor.gif?itemid=11829035",
			"https://media1.tenor.com/images/9ae17e23dee385025730f256cc475a96/tenor.gif?itemid=16874198",
			"https://media1.tenor.com/images/fdc1a977e6880e1cd635a4e416305cd2/tenor.gif?itemid=17012003",
			"https://media1.tenor.com/images/d14969a21a96ec46f61770c50fccf24f/tenor.gif?itemid=5509136",
			"https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956",
			"https://media1.tenor.com/images/af36628688f5f50f297c5e4bce61a35c/tenor.gif?itemid=17314633",
			"https://media1.tenor.com/images/dcd359a74e32bca7197de46a58ec7b72/tenor.gif?itemid=12396060",
			"https://media1.tenor.com/images/4a6b15b8d111255c77da57c735c79b44/tenor.gif?itemid=10937039",
			"https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif?itemid=7958720",
			"https://media1.tenor.com/images/92ec42af8364dcc44816a4f2bb1dd0da/tenor.gif?itemid=16881889",
			"https://media1.tenor.com/images/153b2f1bfd3c595c920ce60f1553c5f7/tenor.gif?itemid=10936993",
			"https://media1.tenor.com/images/e8f880b13c17d61810ac381b2f6a93c3/tenor.gif?itemid=17897236",
			"https://media1.tenor.com/images/299366efafc95bc46bfd2f9c9a46541a/tenor.gif?itemid=16819981",
			"https://media1.tenor.com/images/b797dce439faddabca83352b2c2de550/tenor.gif?itemid=17897223",
			"https://media1.tenor.com/images/45e7f853b25443ffeb86262405c1fc7a/tenor.gif?itemid=16049280",
			"https://media1.tenor.com/images/30c9c3185e1a105571eda9b417986509/tenor.gif?itemid=17208768",
			]
			slap.set_image(url = random.choice(slap_gif))
			await ctx.send(embed = slap)
		else:
			slap = Embed(
				description = message,
				color = (0xa451d8))
			slap_gif = [            #30
			"https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
			"https://media1.tenor.com/images/e846e892dc50a12bd323ff79690f2050/tenor.gif?itemid=19594595",
			"https://media1.tenor.com/images/1125596130202a28802dd2fe20804426/tenor.gif?itemid=17897244",
			"https://media1.tenor.com/images/74db8b0b64e8d539aebebfbb2094ae84/tenor.gif?itemid=15144612",
			"https://media1.tenor.com/images/53d180f129f51575a46b6d3f0f5eeeea/tenor.gif?itemid=5373994",
			"https://media1.tenor.com/images/7437caf9fb0bea289a5bb163b90163c7/tenor.gif?itemid=13595529",
			"https://media1.tenor.com/images/b221fb3f50f0e15b3ace6a2b87ad0ffa/tenor.gif?itemid=8576304",
			"https://media1.tenor.com/images/07b4516d50406b4a320269d514876170/tenor.gif?itemid=17897216",
			"https://media1.tenor.com/images/f7f0d538542373e7e5366b281d3772e7/tenor.gif?itemid=17303228",
			"https://media1.tenor.com/images/6e27186637897c41ac8fcc407521ab11/tenor.gif?itemid=16412212",
			"https://media1.tenor.com/images/ce295550c5436b7b61edac89b3a49b07/tenor.gif?itemid=16335313",
			"https://media1.tenor.com/images/0892a52155ac70d401126ede4d46ed5e/tenor.gif?itemid=12946466",
			"https://media1.tenor.com/images/55be806f33223b4cf185ccfbadca6a0a/tenor.gif?itemid=20504868",
			"https://media1.tenor.com/images/b3348f0f97514f50b9449d63fc343fe3/tenor.gif?itemid=8065158",
			"https://media1.tenor.com/images/cd9559dc9ffc589137b877028bf93176/tenor.gif?itemid=12803383",
			"https://media1.tenor.com/images/6138bdbf998fde7638b8362499ac5427/tenor.gif?itemid=11829035",
			"https://media1.tenor.com/images/9ae17e23dee385025730f256cc475a96/tenor.gif?itemid=16874198",
			"https://media1.tenor.com/images/fdc1a977e6880e1cd635a4e416305cd2/tenor.gif?itemid=17012003",
			"https://media1.tenor.com/images/d14969a21a96ec46f61770c50fccf24f/tenor.gif?itemid=5509136",
			"https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956",
			"https://media1.tenor.com/images/af36628688f5f50f297c5e4bce61a35c/tenor.gif?itemid=17314633",
			"https://media1.tenor.com/images/dcd359a74e32bca7197de46a58ec7b72/tenor.gif?itemid=12396060",
			"https://media1.tenor.com/images/4a6b15b8d111255c77da57c735c79b44/tenor.gif?itemid=10937039",
			"https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif?itemid=7958720",
			"https://media1.tenor.com/images/92ec42af8364dcc44816a4f2bb1dd0da/tenor.gif?itemid=16881889",
			"https://media1.tenor.com/images/153b2f1bfd3c595c920ce60f1553c5f7/tenor.gif?itemid=10936993",
			"https://media1.tenor.com/images/e8f880b13c17d61810ac381b2f6a93c3/tenor.gif?itemid=17897236",
			"https://media1.tenor.com/images/299366efafc95bc46bfd2f9c9a46541a/tenor.gif?itemid=16819981",
			"https://media1.tenor.com/images/b797dce439faddabca83352b2c2de550/tenor.gif?itemid=17897223",
			"https://media1.tenor.com/images/45e7f853b25443ffeb86262405c1fc7a/tenor.gif?itemid=16049280",
			"https://media1.tenor.com/images/30c9c3185e1a105571eda9b417986509/tenor.gif?itemid=17208768",
			]
			slap.set_image(url = random.choice(slap_gif))
			await ctx.send(embed = slap)


	@slap.error
	async def slap_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.", aliases = ["hit",])
	# @is_owner()
	async def punch(self, ctx, member: Member, *, message:Optional[str]):
		if member == ctx.author:
			await ctx.send(f"Why would you punch yourself {ctx.author.display_name}? Do you want a hug?")
		elif not message:
			if ctx.author.id == 424486126351417344:
				punch = Embed(
					description = f"{ctx.author.mention} punches {member.mention}. Its super effective!",
					color = (0xa451d8)
				)
				punch_gif = [                 #20
				"https://media1.tenor.com/images/2b5d7bb1dd4a8e64869c33499c409582/tenor.gif?itemid=9509158",
				"https://media1.tenor.com/images/a7a67336a11b60d292179be1246240c9/tenor.gif?itemid=17175633",
				"https://media1.tenor.com/images/8789543a04274a720b13b1af69a25867/tenor.gif?itemid=12250021",
				"https://media1.tenor.com/images/2e36b49b3d26d1e2fe014e5d4c1dbc75/tenor.gif?itemid=15580060",
				"https://media1.tenor.com/images/abb5363c1f59268e3f94521247eace30/tenor.gif?itemid=16346949",
				"https://media1.tenor.com/images/f03329d8877abfde62b1e056953724f3/tenor.gif?itemid=13785833", 
				"https://media1.tenor.com/images/2487a7679b3d7d23cadcd51381635467/tenor.gif?itemid=11451829",
				"https://media1.tenor.com/images/b111863f0714504a8ba22a0c68e78f32/tenor.gif?itemid=12373244",
				"https://media1.tenor.com/images/99189c9eeb18be326a4d691c6ebd5888/tenor.gif?itemid=17509189",
				"https://media1.tenor.com/images/b746bc37f2e29185523b1b7a0df45fdd/tenor.gif?itemid=19285337",
				"https://media1.tenor.com/images/ee3f2a6939a68df9563a7374f131fd96/tenor.gif?itemid=14210784",
				"https://media1.tenor.com/images/6afcfbc435b698fa5ceb2ff019718e6d/tenor.gif?itemid=10480971",
				"https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446",
				"https://media1.tenor.com/images/19ecddffb14e87a4b6277a9fdb18b8e0/tenor.gif?itemid=15018384",
				"https://media1.tenor.com/images/ce04fdc2e6d0242319f9342d4c929cca/tenor.gif?itemid=20094842",
				"https://cdn.weeb.sh/images/rJHLDT-Wz.gif",
				"https://cdn.weeb.sh/images/BJg7wTbbM.gif",
				"https://media1.tenor.com/images/c7d7777c6dd325d783e74971884ad3d3/tenor.gif?itemid=17308520",
				"https://media1.tenor.com/images/60b8d7a2ca6d419a9fcabfc4eb0bc607/tenor.gif?itemid=18620752",
				"https://media1.tenor.com/images/39400e2b4d93884fd3504fa803f6828e/tenor.gif?itemid=12956632",
				"https://cdn.weeb.sh/images/rJRUk2PLz.gif",
				]
				punch.set_image(url = random.choice(punch_gif))
				await ctx.send(embed = punch)
		
			else:
				punch = Embed(
					description = f"{ctx.author.mention} punches {member.mention}. Its not very effective.",
					color = (0xa451d8)
				)
				punch_gif = [                 #20
				"https://media1.tenor.com/images/2b5d7bb1dd4a8e64869c33499c409582/tenor.gif?itemid=9509158",
				"https://media1.tenor.com/images/a7a67336a11b60d292179be1246240c9/tenor.gif?itemid=17175633",
				"https://media1.tenor.com/images/8789543a04274a720b13b1af69a25867/tenor.gif?itemid=12250021",
				"https://media1.tenor.com/images/2e36b49b3d26d1e2fe014e5d4c1dbc75/tenor.gif?itemid=15580060",
				"https://media1.tenor.com/images/abb5363c1f59268e3f94521247eace30/tenor.gif?itemid=16346949",
				"https://media1.tenor.com/images/f03329d8877abfde62b1e056953724f3/tenor.gif?itemid=13785833", 
				"https://media1.tenor.com/images/2487a7679b3d7d23cadcd51381635467/tenor.gif?itemid=11451829",
				"https://media1.tenor.com/images/b111863f0714504a8ba22a0c68e78f32/tenor.gif?itemid=12373244",
				"https://media1.tenor.com/images/99189c9eeb18be326a4d691c6ebd5888/tenor.gif?itemid=17509189",
				"https://media1.tenor.com/images/b746bc37f2e29185523b1b7a0df45fdd/tenor.gif?itemid=19285337",
				"https://media1.tenor.com/images/ee3f2a6939a68df9563a7374f131fd96/tenor.gif?itemid=14210784",
				"https://media1.tenor.com/images/6afcfbc435b698fa5ceb2ff019718e6d/tenor.gif?itemid=10480971",
				"https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446",
				"https://media1.tenor.com/images/19ecddffb14e87a4b6277a9fdb18b8e0/tenor.gif?itemid=15018384",
				"https://media1.tenor.com/images/ce04fdc2e6d0242319f9342d4c929cca/tenor.gif?itemid=20094842",
				"https://cdn.weeb.sh/images/rJHLDT-Wz.gif",
				"https://cdn.weeb.sh/images/BJg7wTbbM.gif",
				"https://media1.tenor.com/images/c7d7777c6dd325d783e74971884ad3d3/tenor.gif?itemid=17308520",
				"https://media1.tenor.com/images/60b8d7a2ca6d419a9fcabfc4eb0bc607/tenor.gif?itemid=18620752",
				"https://media1.tenor.com/images/39400e2b4d93884fd3504fa803f6828e/tenor.gif?itemid=12956632",
				"https://cdn.weeb.sh/images/rJRUk2PLz.gif",
				]
				punch.set_image(url = random.choice(punch_gif))
				await ctx.send(embed = punch)

		else:
			punch = Embed(
				description = message,
				color = (0xa451d8)
			)
			punch_gif = [                 #20
			"https://media1.tenor.com/images/2b5d7bb1dd4a8e64869c33499c409582/tenor.gif?itemid=9509158",
			"https://media1.tenor.com/images/a7a67336a11b60d292179be1246240c9/tenor.gif?itemid=17175633",
			"https://media1.tenor.com/images/8789543a04274a720b13b1af69a25867/tenor.gif?itemid=12250021",
			"https://media1.tenor.com/images/2e36b49b3d26d1e2fe014e5d4c1dbc75/tenor.gif?itemid=15580060",
			"https://media1.tenor.com/images/abb5363c1f59268e3f94521247eace30/tenor.gif?itemid=16346949",
			"https://media1.tenor.com/images/f03329d8877abfde62b1e056953724f3/tenor.gif?itemid=13785833", 
			"https://media1.tenor.com/images/2487a7679b3d7d23cadcd51381635467/tenor.gif?itemid=11451829",
			"https://media1.tenor.com/images/b111863f0714504a8ba22a0c68e78f32/tenor.gif?itemid=12373244",
			"https://media1.tenor.com/images/99189c9eeb18be326a4d691c6ebd5888/tenor.gif?itemid=17509189",
			"https://media1.tenor.com/images/b746bc37f2e29185523b1b7a0df45fdd/tenor.gif?itemid=19285337",
			"https://media1.tenor.com/images/ee3f2a6939a68df9563a7374f131fd96/tenor.gif?itemid=14210784",
			"https://media1.tenor.com/images/6afcfbc435b698fa5ceb2ff019718e6d/tenor.gif?itemid=10480971",
			"https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446",
			"https://media1.tenor.com/images/19ecddffb14e87a4b6277a9fdb18b8e0/tenor.gif?itemid=15018384",
			"https://media1.tenor.com/images/ce04fdc2e6d0242319f9342d4c929cca/tenor.gif?itemid=20094842",
			"https://cdn.weeb.sh/images/rJHLDT-Wz.gif",
			"https://cdn.weeb.sh/images/BJg7wTbbM.gif",
			"https://media1.tenor.com/images/c7d7777c6dd325d783e74971884ad3d3/tenor.gif?itemid=17308520",
			"https://media1.tenor.com/images/60b8d7a2ca6d419a9fcabfc4eb0bc607/tenor.gif?itemid=18620752",
			"https://media1.tenor.com/images/39400e2b4d93884fd3504fa803f6828e/tenor.gif?itemid=12956632",
			"https://cdn.weeb.sh/images/rJRUk2PLz.gif",
			]
			punch.set_image(url = random.choice(punch_gif))
			await ctx.send(embed = punch)

	@punch.error
	async def punch_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def bully(self, ctx, member: Member, *, message:Optional[str]):
		if member == ctx.author:
			await ctx.send(f"Why would you bully yourself {ctx.author.display_name}?")
		elif not message:
			bully = Embed(
				description = f"{ctx.author.mention} bullies {member.mention}.",
				color = (0xa451d8)
			)
			bully_gif = [          #20
			"https://imgur.com/meZ0TDz.gif",
			"https://media1.tenor.com/images/dd21cc59a6daa2f1b7445c3c20d328d4/tenor.gif?itemid=4703404",
			"https://media1.tenor.com/images/d8eb944ec458745740bf455cc6d50c9f/tenor.gif?itemid=12354084",
			"https://media1.tenor.com/images/361a7789e990551e4f046348550a4186/tenor.gif?itemid=18416219",
			"https://media1.tenor.com/images/a67eb981bfda1c87e06f80b4cab2b98c/tenor.gif?itemid=5707440",
			"https://media1.tenor.com/images/a03478dc88a3f1c15469e584c971e0c8/tenor.gif?itemid=19175962",
			"https://imgur.com/pO2smzw.gif",
			"https://imgur.com/D8SIe4Z.gif",
			"https://imgur.com/jI8zhH6.gif",
			"https://imgur.com/3SsZUVT.gif",
			"https://imgur.com/Lbzh24f.gif",
			"https://imgur.com/a3upumA.gif",
			"https://imgur.com/eP7NKy7.gif",
			"https://imgur.com/g005tMV.gif",
			"https://imgur.com/wzn0ghV.gif",
			"https://imgur.com/meZ0TDz.gif",
			"https://imgur.com/UYKs7Q1.gif",
			"https://imgur.com/xmj8XRD.gif",
			"https://media1.tenor.com/images/6aed717e7ee03adc32d0416c710ac8f9/tenor.gif?itemid=20615896",
			"https://media1.tenor.com/images/b5c2b3c76098d718664578392d7c223f/tenor.gif?itemid=20766207",
			]
			bully.set_image(url = random.choice(bully_gif))
			await ctx.send(embed = bully)
		else:
			bully = Embed(
				description = message,
				color = (0xa451d8)
			)
			bully_gif = [          #20
			"https://imgur.com/meZ0TDz.gif",
			"https://media1.tenor.com/images/dd21cc59a6daa2f1b7445c3c20d328d4/tenor.gif?itemid=4703404",
			"https://media1.tenor.com/images/d8eb944ec458745740bf455cc6d50c9f/tenor.gif?itemid=12354084",
			"https://media1.tenor.com/images/361a7789e990551e4f046348550a4186/tenor.gif?itemid=18416219",
			"https://media1.tenor.com/images/a67eb981bfda1c87e06f80b4cab2b98c/tenor.gif?itemid=5707440",
			"https://media1.tenor.com/images/a03478dc88a3f1c15469e584c971e0c8/tenor.gif?itemid=19175962",
			"https://imgur.com/pO2smzw.gif",
			"https://imgur.com/D8SIe4Z.gif",
			"https://imgur.com/jI8zhH6.gif",
			"https://imgur.com/3SsZUVT.gif",
			"https://imgur.com/Lbzh24f.gif",
			"https://imgur.com/a3upumA.gif",
			"https://imgur.com/eP7NKy7.gif",
			"https://imgur.com/g005tMV.gif",
			"https://imgur.com/wzn0ghV.gif",
			"https://imgur.com/meZ0TDz.gif",
			"https://imgur.com/UYKs7Q1.gif",
			"https://imgur.com/xmj8XRD.gif",
			"https://media1.tenor.com/images/6aed717e7ee03adc32d0416c710ac8f9/tenor.gif?itemid=20615896",
			"https://media1.tenor.com/images/b5c2b3c76098d718664578392d7c223f/tenor.gif?itemid=20766207",
			]
			bully.set_image(url = random.choice(bully_gif))
			await ctx.send(embed = bully)

	@bully.error
	async def bully_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def lick(self, ctx, member: Member, *, message:Optional[str]):
		if member == ctx.author:
			await ctx.send(f"Stop licking yourself {ctx.author.display_name}. Feels weird...")
		elif not message:
			lick = Embed(
				description = f"{ctx.author.mention} is licking {member.mention}. How lewd...",
				color = (0xa451d8)
			)
			lick_gif = [                      #15
			"https://media1.tenor.com/images/5c5828e51733c8ffe1c368f1395a03d0/tenor.gif?itemid=14231351",
			"https://media1.tenor.com/images/5f73f2a7b302a3800b3613095f8a5c40/tenor.gif?itemid=10005495",
			"https://media1.tenor.com/images/c4e7f19ec6bc342c2e7d69caec637783/tenor.gif?itemid=16854581",
			"https://media1.tenor.com/images/5b94662a631d4276cf135b274f0ce9af/tenor.gif?itemid=14848171",
			"https://media1.tenor.com/images/4626d4bbe60ef15212e3181f11d6704a/tenor.gif?itemid=13451633",
			"https://media1.tenor.com/images/b08b6d61bcf16bee7d56408f61855f35/tenor.gif?itemid=17549074",
			"https://media1.tenor.com/images/dbc120cf518319ffe2aedf635ad2df93/tenor.gif?itemid=16600144",
			"https://media1.tenor.com/images/21c8ff8307eb88bf8bf8438e4c78382b/tenor.gif?itemid=16943447",
			"https://media1.tenor.com/images/dbc120cf518319ffe2aedf635ad2df93/tenor.gif?itemid=16600144",
			"https://media1.tenor.com/images/feeef4685f9307b76c78a22ba0a69f48/tenor.gif?itemid=8413059",
			"https://media1.tenor.com/images/1a2d051f28155db0e4cf175d987cdac2/tenor.gif?itemid=12141721",
			"https://media1.tenor.com/images/1925e468ff1ac9efc2100a3d092c54ff/tenor.gif?itemid=4718221",
			"https://media1.tenor.com/images/ec2ca0bf12d7b1a30fea702b59e5a7fa/tenor.gif?itemid=13417195",
			"https://media1.tenor.com/images/b00d152c5645975a06c4916e360635ef/tenor.gif?itemid=15900643",
			"https://media1.tenor.com/images/efd46743771a78e493e66b5d26cd2af1/tenor.gif?itemid=14002773",
			]
			lick.set_image(url = random.choice(lick_gif))
			await ctx.send(embed = lick)
		else:
			lick = Embed(
				description = message,
				color = (0xa451d8)
			)
			lick_gif = [                      #15
			"https://media1.tenor.com/images/5c5828e51733c8ffe1c368f1395a03d0/tenor.gif?itemid=14231351",
			"https://media1.tenor.com/images/5f73f2a7b302a3800b3613095f8a5c40/tenor.gif?itemid=10005495",
			"https://media1.tenor.com/images/c4e7f19ec6bc342c2e7d69caec637783/tenor.gif?itemid=16854581",
			"https://media1.tenor.com/images/5b94662a631d4276cf135b274f0ce9af/tenor.gif?itemid=14848171",
			"https://media1.tenor.com/images/4626d4bbe60ef15212e3181f11d6704a/tenor.gif?itemid=13451633",
			"https://media1.tenor.com/images/b08b6d61bcf16bee7d56408f61855f35/tenor.gif?itemid=17549074",
			"https://media1.tenor.com/images/dbc120cf518319ffe2aedf635ad2df93/tenor.gif?itemid=16600144",
			"https://media1.tenor.com/images/21c8ff8307eb88bf8bf8438e4c78382b/tenor.gif?itemid=16943447",
			"https://media1.tenor.com/images/dbc120cf518319ffe2aedf635ad2df93/tenor.gif?itemid=16600144",
			"https://media1.tenor.com/images/feeef4685f9307b76c78a22ba0a69f48/tenor.gif?itemid=8413059",
			"https://media1.tenor.com/images/1a2d051f28155db0e4cf175d987cdac2/tenor.gif?itemid=12141721",
			"https://media1.tenor.com/images/1925e468ff1ac9efc2100a3d092c54ff/tenor.gif?itemid=4718221",
			"https://media1.tenor.com/images/ec2ca0bf12d7b1a30fea702b59e5a7fa/tenor.gif?itemid=13417195",
			"https://media1.tenor.com/images/b00d152c5645975a06c4916e360635ef/tenor.gif?itemid=15900643",
			"https://media1.tenor.com/images/efd46743771a78e493e66b5d26cd2af1/tenor.gif?itemid=14002773",
			]
			lick.set_image(url = random.choice(lick_gif))
			await ctx.send(embed = lick)

	@lick.error
	async def lick_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.", aliases = ["nom",])
	# @is_owner()
	async def bite(self, ctx, member: Member, *, message:Optional[str]):
		if member == ctx.author:
			await ctx.send(f"Stop biting yourself {ctx.author.display_name}!")
		elif not message:
			bite = Embed(
				description = f"{ctx.author.mention} is biting {member.mention}.",
				color = (0xa451d8)
			)
			bite_gif = [
			"https://media1.tenor.com/images/128c1cfb7f4e6ea4a4dce9b487648143/tenor.gif?itemid=12051598",
			"https://media1.tenor.com/images/1169d1ab96669e13062c1b23ce5b9b01/tenor.gif?itemid=9035033",
			"https://media1.tenor.com/images/f308e2fe3f1b3a41754727f8629e5b56/tenor.gif?itemid=12390216",
			"https://media1.tenor.com/images/8409bd65be28e7bcc5a7630c4ebbdcca/tenor.gif?itemid=15992229",
			"https://media1.tenor.com/images/432a41a6beb3c05953c769686e8c4ce9/tenor.gif?itemid=4704665",
			"https://media1.tenor.com/images/785facc91db815ae613926cddb899ed4/tenor.gif?itemid=17761094",
			"https://media1.tenor.com/images/7afe518504b71a3ca71770f8ac58b73a/tenor.gif?itemid=12897780",
			"https://media1.tenor.com/images/418a2765b0bf54eb57bab3fde5d83a05/tenor.gif?itemid=12151511",
			"https://media1.tenor.com/images/6dd67bd831780c4a754cb33697cddcb6/tenor.gif?itemid=10095819",
			"https://media1.tenor.com/images/6b42070f19e228d7a4ed76d4b35672cd/tenor.gif?itemid=9051585",
			"https://media1.tenor.com/images/06f88667b86a701b1613bbf5fb9205e9/tenor.gif?itemid=13417199",
			"https://media1.tenor.com/images/0d192209c8e9bcd9826af63ba72fc584/tenor.gif?itemid=15164408",
			"https://media1.tenor.com/images/0ef267ee9b49917f3b6436a4e78faa4c/tenor.gif?itemid=11993524",
			"https://media1.tenor.com/images/a74770936aa6f1a766f9879b8bf1ec6b/tenor.gif?itemid=4676912",
			"https://media1.tenor.com/images/91072b9c5b88b668ca2b002d473c9337/tenor.gif?itemid=15793165",
			"https://media1.tenor.com/images/49c23b25f05b791cf7149ba3cc0f2dde/tenor.gif?itemid=14987144",
			"https://media1.tenor.com/images/3baeaa0c5ae3a1a4ae9ac2780b2d965d/tenor.gif?itemid=13342683",
			"https://media1.tenor.com/images/ebc0cf14de0e77473a3fc00e60a2a9d3/tenor.gif?itemid=11535890",
			"https://media1.tenor.com/images/44e0b876f6de97572a2cedacf27c64d8/tenor.gif?itemid=20465324",
			"https://media1.tenor.com/images/2bc0ef61c59cada5e8653947f1e8035c/tenor.gif?itemid=16088516",
			]
			bite.set_image(url = random.choice(bite_gif))
			await ctx.send(embed = bite)
		else:
			bite = Embed(
				description = message,
				color = (0xa451d8)
			)
			bite_gif = [
			"https://media1.tenor.com/images/128c1cfb7f4e6ea4a4dce9b487648143/tenor.gif?itemid=12051598",
			"https://media1.tenor.com/images/1169d1ab96669e13062c1b23ce5b9b01/tenor.gif?itemid=9035033",
			"https://media1.tenor.com/images/f308e2fe3f1b3a41754727f8629e5b56/tenor.gif?itemid=12390216",
			"https://media1.tenor.com/images/8409bd65be28e7bcc5a7630c4ebbdcca/tenor.gif?itemid=15992229",
			"https://media1.tenor.com/images/432a41a6beb3c05953c769686e8c4ce9/tenor.gif?itemid=4704665",
			"https://media1.tenor.com/images/785facc91db815ae613926cddb899ed4/tenor.gif?itemid=17761094",
			"https://media1.tenor.com/images/7afe518504b71a3ca71770f8ac58b73a/tenor.gif?itemid=12897780",
			"https://media1.tenor.com/images/418a2765b0bf54eb57bab3fde5d83a05/tenor.gif?itemid=12151511",
			"https://media1.tenor.com/images/6dd67bd831780c4a754cb33697cddcb6/tenor.gif?itemid=10095819",
			"https://media1.tenor.com/images/6b42070f19e228d7a4ed76d4b35672cd/tenor.gif?itemid=9051585",
			"https://media1.tenor.com/images/06f88667b86a701b1613bbf5fb9205e9/tenor.gif?itemid=13417199",
			"https://media1.tenor.com/images/0d192209c8e9bcd9826af63ba72fc584/tenor.gif?itemid=15164408",
			"https://media1.tenor.com/images/0ef267ee9b49917f3b6436a4e78faa4c/tenor.gif?itemid=11993524",
			"https://media1.tenor.com/images/a74770936aa6f1a766f9879b8bf1ec6b/tenor.gif?itemid=4676912",
			"https://media1.tenor.com/images/91072b9c5b88b668ca2b002d473c9337/tenor.gif?itemid=15793165",
			"https://media1.tenor.com/images/49c23b25f05b791cf7149ba3cc0f2dde/tenor.gif?itemid=14987144",
			"https://media1.tenor.com/images/3baeaa0c5ae3a1a4ae9ac2780b2d965d/tenor.gif?itemid=13342683",
			"https://media1.tenor.com/images/ebc0cf14de0e77473a3fc00e60a2a9d3/tenor.gif?itemid=11535890",
			"https://media1.tenor.com/images/44e0b876f6de97572a2cedacf27c64d8/tenor.gif?itemid=20465324",
			"https://media1.tenor.com/images/2bc0ef61c59cada5e8653947f1e8035c/tenor.gif?itemid=16088516",
			]
			bite.set_image(url = random.choice(bite_gif))
			await ctx.send(embed = bite)

	@bite.error
	async def bite_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def highfive(self, ctx, member: Member, *, message:Optional[str]):
		if member == ctx.author:
			await ctx.send(f"{ctx.author.display_name} sorry I dont know how that works.")
		elif not message:
			highfive = Embed(
				description = f"{ctx.author.mention} gives {member.mention} a highfive.",
				color = (0xa451d8)
			)
			highfive_gif = [
			"https://media1.tenor.com/images/ad22432b945ea3676ffb16ea2989b41b/tenor.gif?itemid=19685271",
			"https://media1.tenor.com/images/7b1f06eac73c36721912edcaacddf666/tenor.gif?itemid=10559431",
			"https://media1.tenor.com/images/459842c03431f2c533dff985ac116f25/tenor.gif?itemid=19803970",
			"https://media1.tenor.com/images/9730876547cb3939388cf79b8a641da9/tenor.gif?itemid=8073516",
			"https://media1.tenor.com/images/6789a03b903af9666077ef4e23c45e3a/tenor.gif?itemid=20003855",
			"https://media1.tenor.com/images/c3263b8196afc25ddc1d53a4224347cd/tenor.gif?itemid=9443275",
			"https://media1.tenor.com/images/16267f3a34efb42598bd822effaccd11/tenor.gif?itemid=14137081",
			"https://media1.tenor.com/images/0c23b320822afd5b1ce3faf01c2b9b69/tenor.gif?itemid=14137078",
			"https://media1.tenor.com/images/ce85a2843f52309b85515f56a0a49d06/tenor.gif?itemid=14137077",
			"https://media1.tenor.com/images/e553e6d366ab4db4590bacc2ac9a4910/tenor.gif?itemid=16059180",
			"https://media1.tenor.com/images/e96d2396570a2fadd9c83e284a1ca675/tenor.gif?itemid=5390726",
			"https://media1.tenor.com/images/b24854d8f00780c1c3920868e74a4946/tenor.gif?itemid=5374002",
			"https://media1.tenor.com/images/106c8e64e864230341b59cc892b5a980/tenor.gif?itemid=5682921",
			"https://media1.tenor.com/images/e2f299d05a7b1832314ec7a331440d4e/tenor.gif?itemid=5374033",
			"https://media1.tenor.com/images/ed9317f7a9b6a057e6d5a39aaa607b80/tenor.gif?itemid=15746517",
			"https://cdn.weeb.sh/images/rJenY1XsW.gif",
			"https://cdn.weeb.sh/images/rJYQt1mjZ.gif",
			"https://cdn.weeb.sh/images/r1MMK1msb.gif",
			"https://cdn.weeb.sh/images/H1Lj9ymsW.gif",
			"https://cdn.weeb.sh/images/BJnxKJXsZ.gif",
			]
			highfive.set_image(url = random.choice(highfive_gif))
			await ctx.send(embed = highfive)
		else:
			highfive = Embed(
				description = message,
				color = (0xa451d8)
			)
			highfive_gif = [
			"https://media1.tenor.com/images/ad22432b945ea3676ffb16ea2989b41b/tenor.gif?itemid=19685271",
			"https://media1.tenor.com/images/7b1f06eac73c36721912edcaacddf666/tenor.gif?itemid=10559431",
			"https://media1.tenor.com/images/459842c03431f2c533dff985ac116f25/tenor.gif?itemid=19803970",
			"https://media1.tenor.com/images/9730876547cb3939388cf79b8a641da9/tenor.gif?itemid=8073516",
			"https://media1.tenor.com/images/6789a03b903af9666077ef4e23c45e3a/tenor.gif?itemid=20003855",
			"https://media1.tenor.com/images/c3263b8196afc25ddc1d53a4224347cd/tenor.gif?itemid=9443275",
			"https://media1.tenor.com/images/16267f3a34efb42598bd822effaccd11/tenor.gif?itemid=14137081",
			"https://media1.tenor.com/images/0c23b320822afd5b1ce3faf01c2b9b69/tenor.gif?itemid=14137078",
			"https://media1.tenor.com/images/ce85a2843f52309b85515f56a0a49d06/tenor.gif?itemid=14137077",
			"https://media1.tenor.com/images/e553e6d366ab4db4590bacc2ac9a4910/tenor.gif?itemid=16059180",
			"https://media1.tenor.com/images/e96d2396570a2fadd9c83e284a1ca675/tenor.gif?itemid=5390726",
			"https://media1.tenor.com/images/b24854d8f00780c1c3920868e74a4946/tenor.gif?itemid=5374002",
			"https://media1.tenor.com/images/106c8e64e864230341b59cc892b5a980/tenor.gif?itemid=5682921",
			"https://media1.tenor.com/images/e2f299d05a7b1832314ec7a331440d4e/tenor.gif?itemid=5374033",
			"https://media1.tenor.com/images/ed9317f7a9b6a057e6d5a39aaa607b80/tenor.gif?itemid=15746517",
			"https://cdn.weeb.sh/images/rJenY1XsW.gif",
			"https://cdn.weeb.sh/images/rJYQt1mjZ.gif",
			"https://cdn.weeb.sh/images/r1MMK1msb.gif",
			"https://cdn.weeb.sh/images/H1Lj9ymsW.gif",
			"https://cdn.weeb.sh/images/BJnxKJXsZ.gif",
			]
			highfive.set_image(url = random.choice(highfive_gif))
			await ctx.send(embed = highfive)

	@highfive.error
	async def highfive_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def tickle(self, ctx, member: Member, *, message:Optional[str]):
		if member == ctx.author:
			await ctx.send(f"{ctx.author.display_name} you can't tickle yourself silly.")
		elif not message:
			tickle = Embed(
				description = f"{ctx.author.mention} is tickling {member.mention}. >.<",
				color = (0xa451d8)
			)
			tickle_gif = [             #20
			"https://media1.tenor.com/images/f43da23b4ed0938ce362b0374b88e42c/tenor.gif?itemid=8054679",
			"https://media1.tenor.com/images/05a64a05e5501be2b1a5a734998ad2b2/tenor.gif?itemid=11379130",
			"https://media1.tenor.com/images/fea79fed0168efcaf1ddfb14d8af1a6d/tenor.gif?itemid=7283507",
			"https://media1.tenor.com/images/eaef77278673333265da087f65941e48/tenor.gif?itemid=16574823",
			"https://media1.tenor.com/images/d38554c6e23b86c81f8d4a3764b38912/tenor.gif?itemid=11379131",
			"https://media1.tenor.com/images/9dc0ea3c8b017694ea73355591e08e66/tenor.gif?itemid=19658422",
			"https://media1.tenor.com/images/02f62186ccb7fa8a2667f3216cfd7e13/tenor.gif?itemid=13269751",
			"https://media1.tenor.com/images/c4106315d0889667a9befbc121747145/tenor.gif?itemid=20218947",
			"https://media1.tenor.com/images/61a7525387502b29292ef74a0c285017/tenor.gif?itemid=20748825",
			"https://media1.tenor.com/images/90f76d0d3e2d333d76a229ec9bfd0d3d/tenor.gif?itemid=12583171",
			"https://media1.tenor.com/images/57e77ff5b5967a0baed92a7a105fbe61/tenor.gif?itemid=17093994",
			"https://cdn.weeb.sh/images/HyjNLkXiZ.gif",
			"https://cdn.weeb.sh/images/SyGQIk7i-.gif",
			"https://cdn.weeb.sh/images/Byj7LJmiW.gif",
			"https://cdn.weeb.sh/images/SkmEI1mjb.gif",
			"https://cdn.weeb.sh/images/rkPzIyQi-.gif",
			"https://cdn.weeb.sh/images/H1p0ByQo-.gif",
			"https://cdn.weeb.sh/images/SyQHUy7oW.gif",
			"https://cdn.weeb.sh/images/rybRByXjZ.gif",
			"https://media1.tenor.com/images/193f5b35611a82dd205d829c75f546f4/tenor.gif?itemid=15515147",
			]
			tickle.set_image(url = random.choice(tickle_gif))
			await ctx.send(embed = tickle)
		else:
			tickle = Embed(
				description = message,
				color = (0xa451d8)
			)
			tickle_gif = [             #20
			"https://media1.tenor.com/images/f43da23b4ed0938ce362b0374b88e42c/tenor.gif?itemid=8054679",
			"https://media1.tenor.com/images/05a64a05e5501be2b1a5a734998ad2b2/tenor.gif?itemid=11379130",
			"https://media1.tenor.com/images/fea79fed0168efcaf1ddfb14d8af1a6d/tenor.gif?itemid=7283507",
			"https://media1.tenor.com/images/eaef77278673333265da087f65941e48/tenor.gif?itemid=16574823",
			"https://media1.tenor.com/images/d38554c6e23b86c81f8d4a3764b38912/tenor.gif?itemid=11379131",
			"https://media1.tenor.com/images/9dc0ea3c8b017694ea73355591e08e66/tenor.gif?itemid=19658422",
			"https://media1.tenor.com/images/02f62186ccb7fa8a2667f3216cfd7e13/tenor.gif?itemid=13269751",
			"https://media1.tenor.com/images/c4106315d0889667a9befbc121747145/tenor.gif?itemid=20218947",
			"https://media1.tenor.com/images/61a7525387502b29292ef74a0c285017/tenor.gif?itemid=20748825",
			"https://media1.tenor.com/images/90f76d0d3e2d333d76a229ec9bfd0d3d/tenor.gif?itemid=12583171",
			"https://media1.tenor.com/images/57e77ff5b5967a0baed92a7a105fbe61/tenor.gif?itemid=17093994",
			"https://cdn.weeb.sh/images/HyjNLkXiZ.gif",
			"https://cdn.weeb.sh/images/SyGQIk7i-.gif",
			"https://cdn.weeb.sh/images/Byj7LJmiW.gif",
			"https://cdn.weeb.sh/images/SkmEI1mjb.gif",
			"https://cdn.weeb.sh/images/rkPzIyQi-.gif",
			"https://cdn.weeb.sh/images/H1p0ByQo-.gif",
			"https://cdn.weeb.sh/images/SyQHUy7oW.gif",
			"https://cdn.weeb.sh/images/rybRByXjZ.gif",
			"https://media1.tenor.com/images/193f5b35611a82dd205d829c75f546f4/tenor.gif?itemid=15515147",
			]
			tickle.set_image(url = random.choice(tickle_gif))
			await ctx.send(embed = tickle)

	@tickle.error
	async def tickle_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.", aliases = ["thinking", "thonking"])
	# @is_owner()
	async def hmm(self, ctx):
		hmm = Embed(
			description = f"{ctx.author.mention} is thinking....",
			color = (0xa451d8)
		)
		hmm_gif = [
		"https://media1.tenor.com/images/c229d1dc0689096b4a5d4b743745e303/tenor.gif?itemid=13902070",
		"https://media1.tenor.com/images/813efb9ade453f7f4a67b3ede8c2cbf5/tenor.gif?itemid=16377462",
		"https://media1.tenor.com/images/046c5cfdfb264975a4ed2bb10f71d778/tenor.gif?itemid=5236580",
		"https://media1.tenor.com/images/f26905016548487fd8543b5a753c34c8/tenor.gif?itemid=17275096",
		"https://media1.tenor.com/images/788831460d1d5f9aad96c44d5918189f/tenor.gif?itemid=13705323",
		"https://media1.tenor.com/images/a790e458eb86a4f191536ef9c174d122/tenor.gif?itemid=12396059",
		"https://media1.tenor.com/images/d7c762fc8149db58393f3d31fbddaad1/tenor.gif?itemid=17156744",
		"https://media1.tenor.com/images/2ac745814f286a26f977664f43cebab6/tenor.gif?itemid=19850528",
		"https://media1.tenor.com/images/d714bd812c93374c38427a70cd108476/tenor.gif?itemid=17701916",
		"https://media1.tenor.com/images/04e9d5f6c2f5848a5dc199d6f0190be9/tenor.gif?itemid=12799633",
		"https://media1.tenor.com/images/614bceea7d8e2b435831531681a00532/tenor.gif?itemid=17795306",
		"https://media1.tenor.com/images/f956d7ea4d9b13f197c281e478ef0751/tenor.gif?itemid=13400371",
		"https://media1.tenor.com/images/38fbe37f1404cdd6b9bb30572d997943/tenor.gif?itemid=17795293",
		"https://media1.tenor.com/images/4cd1bb83b560c01c9de142d989c2ef89/tenor.gif?itemid=15282251",
		"https://media1.tenor.com/images/69a5f3068a45aa8a61cfde615b2ae411/tenor.gif?itemid=11970277",
		"https://media1.tenor.com/images/4ca456c6c5d75c1963a41cfa113b1d02/tenor.gif?itemid=20343858",
		"https://media1.tenor.com/images/710a672b4965ccc265b6a7395ec2d150/tenor.gif?itemid=16529740",
		"https://media1.tenor.com/images/5aac34d9adf2fb7775a49c5f42e37f18/tenor.gif?itemid=19553755",
		"https://media1.tenor.com/images/4112422bc71b7d8509b306b82237af4d/tenor.gif?itemid=16870048",
		"https://media1.tenor.com/images/9f9801c1fbec6e421cb45f3f523befe5/tenor.gif?itemid=19812987",
		"https://media1.tenor.com/images/3eacaae1edb30c9cc79a894c1b012bb4/tenor.gif?itemid=18868276",
		"https://media1.tenor.com/images/cecd2a814f8d82e529c933c72737d7d3/tenor.gif?itemid=12390238",
		"https://media1.tenor.com/images/ddfb85ab8255c6a0858251812063b5ef/tenor.gif?itemid=17858119",
		"https://media1.tenor.com/images/36a264ad1e2e094ffe291e19a9f97a23/tenor.gif?itemid=17173072",
		"https://media1.tenor.com/images/a2e9889567a894d48328ebfaf3924de0/tenor.gif?itemid=5206184",
		"https://media1.tenor.com/images/b17071803587b90e03d2d8076bf6ecd5/tenor.gif?itemid=18966875",
		"https://media1.tenor.com/images/383cfea5dbd7d6ccc67a96e8c064a788/tenor.gif?itemid=16025185",
		"https://media1.tenor.com/images/a0d7514499a4925e30a0f6e0f63405a9/tenor.gif?itemid=10431631",
		"https://media1.tenor.com/images/e76349838549bfc1f5d1ae1f3a7013bc/tenor.gif?itemid=15113182",
		"https://media1.tenor.com/images/f5d96bd02a6642105d96044ff9b2f0eb/tenor.gif?itemid=17385224",
		"https://media1.tenor.com/images/16e0f99d3a85aedb03f3bf204e53e39c/tenor.gif?itemid=19736012",
		]
		hmm.set_image(url = random.choice(hmm_gif))
		await ctx.send(embed = hmm)

	@command(aliases= ["shy",], brief = "Action/Emote command.")
	# @is_owner()
	async def blush(self, ctx):
		blush = Embed(
			description = f"{ctx.author.mention} is blushing. Cuteee!",
			color = (0xa451d8)
		)
		blush_gif = [             #20
		"https://media1.tenor.com/images/c2c26fb63d6bf7ef31a7a593645d7ff5/tenor.gif?itemid=13284053",
		"https://media1.tenor.com/images/a7e87466022015e036c06c3927c251f9/tenor.gif?itemid=8971744",
		"https://media1.tenor.com/images/cbfd2a06c6d350e19a0c173dec8dccde/tenor.gif?itemid=15727535",
		"https://media1.tenor.com/images/5ea40ca0d6544dbf9c0074542810e149/tenor.gif?itemid=14841901",
		"https://media1.tenor.com/images/794f8ff2b76326abe77171b3fb21252d/tenor.gif?itemid=11825225",
		"https://media1.tenor.com/images/f72035e032125a5395883b8d68d9df5d/tenor.gif?itemid=16149781",
		"https://media1.tenor.com/images/82b0f0a24e1621510b1216317edd4ba0/tenor.gif?itemid=14119517",
		"https://media1.tenor.com/images/84307582253a96e4552d20e3ecef3a33/tenor.gif?itemid=5531498",
		"https://media1.tenor.com/images/85be0c08818f1faa7cffbbec9cf7c02e/tenor.gif?itemid=4957566",
		"https://media1.tenor.com/images/5eea16dacd36b7080e83bd14d8ecac81/tenor.gif?itemid=13931357",
		"https://media1.tenor.com/images/f72035e032125a5395883b8d68d9df5d/tenor.gif?itemid=16149781",
		"https://media1.tenor.com/images/8f76f034ccc458bd09675c0380f59cb7/tenor.gif?itemid=5634589",
		"https://media1.tenor.com/images/84307582253a96e4552d20e3ecef3a33/tenor.gif?itemid=5531498",
		"https://media1.tenor.com/images/4f270d2727e514056ae63f155ba0cef2/tenor.gif?itemid=13045709",
		"https://media1.tenor.com/images/71015cf10d2bc6ddc6c2dd0d7b294277/tenor.gif?itemid=9096269",
		"https://cdn.weeb.sh/images/rke5DTadPb.gif",
		"https://cdn.weeb.sh/images/BJH4f8mP-.gif",
		"https://cdn.weeb.sh/images/Hy-GGIXvb.gif",
		"https://cdn.weeb.sh/images/SkckMIXP-.gif",
		"https://cdn.weeb.sh/images/rJa-zUmv-.gif",
		]
		blush.set_image(url = random.choice(blush_gif))
		await ctx.send(embed = blush)


	@command(name ="thumbsup", aliases = ["niceguypose"], brief = "Action/Emote command.")
	# @is_owner()
	async def thumbsup(self, ctx):
		thumbsup = Embed(
			description = f"{ctx.author.mention} gives you a thumbsup.",
			color = (0xa451d8)
		)
		thumbsup_gif = [                     #25
		"https://media1.tenor.com/images/650a651cefb981999f0187b798a598a0/tenor.gif?itemid=18109417",
		"https://media1.tenor.com/images/3194434d56c0f9a39813a9209d1dc9a1/tenor.gif?itemid=12390446",
		"https://media1.tenor.com/images/260ad2a18d76c77b9c20722d5df4d0da/tenor.gif?itemid=13721418",
		"https://media1.tenor.com/images/82068b7fd8955991648dbb69f70232e4/tenor.gif?itemid=20546495",
		"https://media1.tenor.com/images/bc58975b4797d945c2cdffe2dda64a0f/tenor.gif?itemid=14088879",
		"https://media1.tenor.com/images/c0674774e1c5538d3e607f000278cbcf/tenor.gif?itemid=11949289",
		"https://media1.tenor.com/images/8f09ac7e19d360397872e04285fdf08a/tenor.gif?itemid=14110281",
		"https://media1.tenor.com/images/4b243eee30492b8f6fc9272f0fc45b47/tenor.gif?itemid=20205505",
		"https://media1.tenor.com/images/0f6168404d57e722b931c39d21e04c37/tenor.gif?itemid=4947346",
		"https://media1.tenor.com/images/6b8d20af6baa2b81930e028e0e231708/tenor.gif?itemid=10138900",
		"https://media1.tenor.com/images/c4923a011eeeab9530257dbe8e9f1e3a/tenor.gif?itemid=13400372",
		"https://media1.tenor.com/images/3496105c1c9027500c102816bdae6ddf/tenor.gif?itemid=14110287",
		"https://media1.tenor.com/images/54e8631b77e3612be9a217ed98961447/tenor.gif?itemid=9911334",
		"https://media1.tenor.com/images/dec0fbbed5494e424f845a2928341d75/tenor.gif?itemid=14739705",
		"https://media1.tenor.com/images/45cc8aa4755310a88cff35f6880f1aaa/tenor.gif?itemid=7659021",
		"https://media1.tenor.com/images/ae8dc8de985cacc2340f10b2b2db0f24/tenor.gif?itemid=9340442",
		"https://media1.tenor.com/images/1a97b46ae10696e276f90876cc3ac23c/tenor.gif?itemid=7563556",
		"https://media1.tenor.com/images/88c7bef5a22617feb5eddeb9cd95808d/tenor.gif?itemid=16582089",
		"https://media1.tenor.com/images/c3d28823aeaddb1bc410698f11b1d882/tenor.gif?itemid=17598625",
		"https://media1.tenor.com/images/b583a94df50e93fa3572c5fe1cd8f059/tenor.gif?itemid=20168124",
		"https://media1.tenor.com/images/a79649fc341ed02445706a592a0c6b46/tenor.gif?itemid=7967630",
		"https://media1.tenor.com/images/81eddbe4a9ea94f171d4bf8d0abc3da7/tenor.gif?itemid=14906939",
		"https://media1.tenor.com/images/5505cdab33345c57d705467db9c09ada/tenor.gif?itemid=20429719",
		"https://media1.tenor.com/images/9305d4c54be8566eb3b9ed00a9fc2f84/tenor.gif?itemid=12836479",
		]
		thumbsup.set_image(url = random.choice(thumbsup_gif))
		await ctx.send(embed = thumbsup)


	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def grin(self, ctx):
		grin = Embed(
			description = f"{ctx.author.mention} has a wide grin.",
			color = (0xa451d8)
		)
		grin_gif = [            #20
		"https://media1.tenor.com/images/64e0528a06b474ffb14525c437da2544/tenor.gif?itemid=11031890",
		"https://media1.tenor.com/images/7c21733e715cee69340a34b2f50be7d0/tenor.gif?itemid=8730349",
		"https://media1.tenor.com/images/2dff8879b3aa16404eedf586827c4085/tenor.gif?itemid=5109617",
		"https://media1.tenor.com/images/683b40a9da270868366b0b43541ec2c7/tenor.gif?itemid=5109317",
		"https://media1.tenor.com/images/a6db0966282e6d21514f305b0c9e6f63/tenor.gif?itemid=12815749",
		"https://media1.tenor.com/images/07c3375ba6d210bb7e7a11017dcc9b5a/tenor.gif?itemid=11098326",
		"https://media1.tenor.com/images/3ee3cddb49bc6536aa94ca593336f0f3/tenor.gif?itemid=5658324",
		"https://media1.tenor.com/images/02cc94ffe6eb5264bed028e35686c4f5/tenor.gif?itemid=18759347",
		"https://media1.tenor.com/images/6759db50d7423fb4e549a50690ee7c39/tenor.gif?itemid=15150246",
		"https://media1.tenor.com/images/adfcd2f9b76416c054e4c9f5f1bca724/tenor.gif?itemid=13138954",
		"https://media1.tenor.com/images/895ea88ae5b22b4774ee5be0b9c17d01/tenor.gif?itemid=16414389",
		"https://media1.tenor.com/images/d68b8ac8d790c09595b5f95148a563fb/tenor.gif?itemid=16634431",
		"https://media1.tenor.com/images/07c3375ba6d210bb7e7a11017dcc9b5a/tenor.gif?itemid=11098326",
		"https://media1.tenor.com/images/f51dba81c54f1ccdc3d63b77c7802a0d/tenor.gif?itemid=5014366",
		"https://cdn.weeb.sh/images/ry4U4JFwW.gif",
		"https://cdn.weeb.sh/images/SJPd4JYPZ.gif",
		"https://cdn.weeb.sh/images/BJ5YNktD-.gif",
		"https://cdn.weeb.sh/images/B1-UN1KPb.gif",
		"https://cdn.weeb.sh/images/S1X7GIXw-.gif",
		]
		grin.set_image(url = random.choice(grin_gif))
		await ctx.send(embed = grin)


	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def smug(self, ctx):
		smug = Embed(
			description = f"{ctx.author.mention} has a smug on their face.",
			color = (0xa451d8)
		)
		smug_gif = [            #20
		"https://media1.tenor.com/images/5917526c0ef2100e56c139b6e4d36e40/tenor.gif?itemid=5677612",
		"https://media1.tenor.com/images/52ea7d449a5402030a3432fd3c94aa99/tenor.gif?itemid=13119051",
		"https://media1.tenor.com/images/7bf80670fd6ea3ad6cff87cddd3c10b5/tenor.gif?itemid=12946334",
		"https://media1.tenor.com/images/123df3be1acfe3306b91e9c3dd6f9438/tenor.gif?itemid=5322596",
		"https://media1.tenor.com/images/6c2243fcf5eec62d6c43e5078c30b1ca/tenor.gif?itemid=10120660",
		"https://media1.tenor.com/images/8bd1588e665e2c33df39736b2d2c0e12/tenor.gif?itemid=12823757",
		"https://media1.tenor.com/images/207b1a3cd83383e095a39b8252238367/tenor.gif?itemid=19376235",
		"https://media1.tenor.com/images/c07ed00c22986003ff6d36d3a43d4edc/tenor.gif?itemid=16004483",
		"https://media1.tenor.com/images/dd9c9b4f677551ccc7429bed6c639e73/tenor.gif?itemid=8917529",
		"https://media1.tenor.com/images/4a8488ebb124b2d6f36dbd34b964e01b/tenor.gif?itemid=6164636",
		"https://media1.tenor.com/images/bea3f6e41c736db4a99c79c64c46104b/tenor.gif?itemid=4382407",
		"https://media1.tenor.com/images/76f7160c04d244a5f34d77d25122344e/tenor.gif?itemid=13598613",
		"https://media1.tenor.com/images/aec4dd57849dc24fbc0487c492b1d3a3/tenor.gif?itemid=14632552",
		"https://media1.tenor.com/images/906bbc85a7820f68a7fc658aeeceb069/tenor.gif?itemid=10195728",
		"https://media1.tenor.com/images/66a6988ccf6e1700458866d4ce664ace/tenor.gif?itemid=14770509",
		"https://media1.tenor.com/images/a7a495be99de980b6bcdb77aa0849c44/tenor.gif?itemid=10358099",
		"https://media1.tenor.com/images/54c781ad45eb7347b07e2207daa08ee5/tenor.gif?itemid=8075676",
		"https://media1.tenor.com/images/0dbc24b7b195bca10dd04e57c3823c64/tenor.gif?itemid=9779997",
		"https://media1.tenor.com/images/58899ca7e0ffa4a785ad23ccda01e082/tenor.gif?itemid=13979455",
		"https://media1.tenor.com/images/0097fa7f957477f9edc5ff147bb9a5ad/tenor.gif?itemid=12390496",
		]
		smug.set_image(url = random.choice(smug_gif))
		await ctx.send(embed = smug)


	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def dance(self, ctx):
		dance = Embed(
			description = f"{ctx.author.mention} started dancing.",
			color = (0xa451d8)
		)
		dance_gif = [           #20
		"https://media1.tenor.com/images/a8b70e6d4459ee9d37ac151380178423/tenor.gif?itemid=4934544",
		"https://media1.tenor.com/images/bab39de2e95b92fe1245835c34fbdd9f/tenor.gif?itemid=10654450",
		"https://media1.tenor.com/images/9690ea2ef066ce46fcfd8784f83905b9/tenor.gif?itemid=15439991",
		"https://media1.tenor.com/images/dab5c81acb05374237f1cc8da1729826/tenor.gif?itemid=11781562",
		"https://media1.tenor.com/images/4f6c135a99c19b17f0156d2584512e55/tenor.gif?itemid=19646014",
		"https://media1.tenor.com/images/c925511d32350cc04411756d623ebad6/tenor.gif?itemid=13462237",
		"https://media1.tenor.com/images/86ed183f271b9b322aef616ed086c8b6/tenor.gif?itemid=4909808",
		"https://media1.tenor.com/images/daa38ff8d98d709e525de49f536ae278/tenor.gif?itemid=11217278",
		"https://media1.tenor.com/images/d85d9011c6c866057ca2e6780c6fedd8/tenor.gif?itemid=13266349",
		"https://media1.tenor.com/images/7627a7009dcd44f40bcf3c168f0c6ad6/tenor.gif?itemid=16108170",
		"https://media1.tenor.com/images/ffadaad9cd88bce23d2127c7072d4884/tenor.gif?itemid=19335462",
		"https://media1.tenor.com/images/b013100cef1cde9158b0371fc1cf7489/tenor.gif?itemid=8074573",
		"https://media1.tenor.com/images/078d0df8e8fc0d28533b647326bf8f3d/tenor.gif?itemid=13706721",
		"https://media1.tenor.com/images/21e860a31f32d5e3e6bdf2963cadfebf/tenor.gif?itemid=5897404",
		"https://media1.tenor.com/images/bb12086e528b3d977d71c69d6ec0ddf5/tenor.gif?itemid=14919611",
		"https://media1.tenor.com/images/9b89ddf1522e582dad4fd7950f0a62be/tenor.gif?itemid=5646380",
		"https://media1.tenor.com/images/bbb1042e932a6d4de8a8daa487cd6fa6/tenor.gif?itemid=14285337",
		"https://media1.tenor.com/images/e7476ea3e752830ba35769c0565daba2/tenor.gif?itemid=13237443",
		"https://cdn.weeb.sh/images/BJoRuLXPW.gif", 
		"https://cdn.weeb.sh/images/HylouUmPb.gif",
		]
		dance.set_image(url = random.choice(dance_gif))
		await ctx.send(embed = dance)


	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def shrug(self, ctx):
		shrug = Embed(
			description = f"{ctx.author.mention} does not care.",
			color = (0xa451d8)
		)
		shrug_gif = [            #20
		"https://media1.tenor.com/images/8bf3267e5f0a00eef84f9fbb6ac4ac1b/tenor.gif?itemid=13119038",
		"https://cdn.weeb.sh/images/r1g4mkKvW.gif",
		"https://media1.tenor.com/images/94898cd48980cfc4128622300a9ba746/tenor.gif?itemid=14913933",
		"https://media1.tenor.com/images/539c646415cfa02b9eabdd55b32c8360/tenor.gif?itemid=14576522",
		"https://media1.tenor.com/images/20ec9ca6d8e391c0863cf80896560c23/tenor.gif?itemid=18057861",
		"https://media1.tenor.com/images/053a9ece4298fbb81f0ae5406e5fc2e3/tenor.gif?itemid=12787691",
		"https://media1.tenor.com/images/1554fbd4900e801651b01d445035cd01/tenor.gif?itemid=13651820",
		"https://media1.tenor.com/images/eee203755d0bc8babc270baa2ca42a1c/tenor.gif?itemid=20442775",
		"https://media1.tenor.com/images/40670e6178780839f9ddae7ae5616589/tenor.gif?itemid=8089057",
		"https://media1.tenor.com/images/ff9daac04b5682278ce656b85c166c68/tenor.gif?itemid=14625512",
		"https://media1.tenor.com/images/450fc417df7728696ed6dab9628a4b6d/tenor.gif?itemid=14604462",
		"https://cdn.weeb.sh/images/HyHk2WSrz.gif",
		"https://cdn.weeb.sh/images/B1hai-HBG.gif",
		"https://media1.tenor.com/images/f168e0109defe801787890fe2a6104bc/tenor.gif?itemid=13951519",
		"https://media1.tenor.com/images/ee1ac585e7606cb0abb54c24bfa46827/tenor.gif?itemid=17198218",
		"https://media1.tenor.com/images/3cae1f29a2fc373efc42b4b88f54c616/tenor.gif?itemid=20844956",
		"https://media1.tenor.com/images/66bc0b4dff185056a2b4a8616b7436a5/tenor.gif?itemid=18062354",
		"https://media1.tenor.com/images/472c2841c3bf7ec962124bed2698a4a4/tenor.gif?itemid=19967022",
		"https://media1.tenor.com/images/450fc417df7728696ed6dab9628a4b6d/tenor.gif?itemid=14604462",
		"https://media1.tenor.com/images/33822751096fc5888d3c0a7e2cff4923/tenor.gif?itemid=20462534",
		]

		shrug.set_image(url = random.choice(shrug_gif))
		await ctx.send(embed = shrug)


	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def smile(self, ctx):
		smile = Embed(
			description = f"{ctx.author.mention} *smiles*.",
			color = (0xa451d8)
		)
		smile_gif = [           #30
		"https://media1.tenor.com/images/b3a91592347d989737bade5966fc6ca2/tenor.gif?itemid=18395216",
		"https://media1.tenor.com/images/005e8df693c0f59e442b0bf95c22d0f5/tenor.gif?itemid=10947495",
		"https://media1.tenor.com/images/c0e1b46577b048c4115e9e8d054f3b27/tenor.gif?itemid=13871420",
		"https://media1.tenor.com/images/55dde6c4f1eaca6b1e52626b980c0074/tenor.gif?itemid=13576447",
		"https://media1.tenor.com/images/cc66ae959cb51c118c782325fcdc4f3f/tenor.gif?itemid=9869247",
		"https://media1.tenor.com/images/4e0a400d7621b5452854bcae00d9a98e/tenor.gif?itemid=5723668",
		"https://media1.tenor.com/images/ba7c28c45c0123e95fbdf0854cbc7861/tenor.gif?itemid=12869746",
		"https://media1.tenor.com/images/c5fad21f9828d19044a58f8b84a6e14b/tenor.gif?itemid=6013419",
		"https://media1.tenor.com/images/82b39c323ca376e9bb5844a54973fc42/tenor.gif?itemid=16596386",
		"https://media1.tenor.com/images/7676a956e0dda07ec7f55d3eacbf353b/tenor.gif?itemid=16072068",
		"https://media1.tenor.com/images/ea548b6de4a49f3875d7f733a5676a94/tenor.gif?itemid=16993925",
		"https://media1.tenor.com/images/325b3ba6a2beabe21c79b54c6de4e2c7/tenor.gif?itemid=15060821",
		"https://media1.tenor.com/images/668d973169acd6d85f899d94f154831c/tenor.gif?itemid=12802172",
		"https://media1.tenor.com/images/ecc8d5665f2698529d63b7c7c55fb5fc/tenor.gif?itemid=8674277",
		"https://media1.tenor.com/images/d5484f103deec4337249bd1654ef4c43/tenor.gif?itemid=17341003",
		"https://media1.tenor.com/images/b3a91592347d989737bade5966fc6ca2/tenor.gif?itemid=18395216",
		"https://media1.tenor.com/images/895ea88ae5b22b4774ee5be0b9c17d01/tenor.gif?itemid=16414389",
		"https://media1.tenor.com/images/148a2f4fbf904d6008ca9c7d71806859/tenor.gif?itemid=17383218",
		"https://media1.tenor.com/images/bb0cbe662c9c7fb3bd59e75a7214475d/tenor.gif?itemid=4795681",
		"https://media1.tenor.com/images/895ea88ae5b22b4774ee5be0b9c17d01/tenor.gif?itemid=16414389",
		"https://cdn.weeb.sh/images/r1IdE1KD-.gif",
		"https://cdn.weeb.sh/images/HJ0DEytPZ.gif",
		"https://cdn.weeb.sh/images/HypVV1Kwb.gif",
		"https://cdn.weeb.sh/images/rkB4NJtD-.gif",
		"https://cdn.weeb.sh/images/HyC_4ytD-.gif",
		"https://cdn.weeb.sh/images/H1RXNJKPZ.gif",
		"https://cdn.weeb.sh/images/rJcE4ytDb.gif",
		"https://cdn.weeb.sh/images/SJBYN1YwZ.gif",
		"https://cdn.weeb.sh/images/SywN41KvW.gif",
		"https://cdn.weeb.sh/images/Bk8P4yKwW.gif",
		]
		smile.set_image(url = random.choice(smile_gif))
		await ctx.send(embed = smile)

	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def cry(self, ctx):
		cry = Embed(
			description = f"{ctx.author.mention} is crying...",
			color = (0xa451d8)
		)
		cry_gif = [             #30
		"https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?itemid=5184314",
		"https://media1.tenor.com/images/80bae566ef056960aed4c7f22494c43b/tenor.gif?itemid=19369337",
		"https://media1.tenor.com/images/b0f4b5f158e8a964adbabd048fb9e556/tenor.gif?itemid=13949015",
		"https://media1.tenor.com/images/c5408a3cf0199a8249ff4249ce28a43e/tenor.gif?itemid=16387431",
		"https://media1.tenor.com/images/2df7b73d06d769bb0ad8ad8596c6d4b1/tenor.gif?itemid=13978386",
		"https://media1.tenor.com/images/8f6da405119d24f7f86ff036d02c2fd4/tenor.gif?itemid=5378935",
		"https://media1.tenor.com/images/ae4138661bc1930d32c0435ef788c456/tenor.gif?itemid=15805005",
		"https://media1.tenor.com/images/d5668af606ca4d0332a6507418cabbce/tenor.gif?itemid=4952249",
		"https://media1.tenor.com/images/031c7c348d3b86296976e2407723d4a8/tenor.gif?itemid=5014031",
		"https://media1.tenor.com/images/4f22255d60f3f19edf9296992b4e3483/tenor.gif?itemid=4772697",
		"https://media1.tenor.com/images/7ef999b077acd6ebef92afc34690097e/tenor.gif?itemid=10893043",
		"https://media1.tenor.com/images/e69ebde3631408c200777ebe10f84367/tenor.gif?itemid=5081296",
		"https://media1.tenor.com/images/d22d5b7c7face2349bcc3c272e3430a7/tenor.gif?itemid=16811598",
		"https://media1.tenor.com/images/5b2bbfcbc1724a0bdc1b48dcf89274d6/tenor.gif?itemid=16648179",
		"https://media1.tenor.com/images/5544c537be7aa645827e1ec2e130c35c/tenor.gif?itemid=5391699",
		"https://media1.tenor.com/images/98466bf4ae57b70548f19863ca7ea2b4/tenor.gif?itemid=14682297",
		"https://media1.tenor.com/images/b88fa314f0f172832a5f41fce111f359/tenor.gif?itemid=13356071",
		"https://media1.tenor.com/images/49e4248f18b359dd46f7b60b01d1a4a0/tenor.gif?itemid=5652241",
		"https://media1.tenor.com/images/ae4138661bc1930d32c0435ef788c456/tenor.gif?itemid=15805005",
		"https://media1.tenor.com/images/67df1dca3260e0032f40048759a967a5/tenor.gif?itemid=5415917",
		"https://media1.tenor.com/images/75edc9882e5175f86c2af777ffbb14a6/tenor.gif?itemid=5755232",
		"https://media1.tenor.com/images/26e7564bfb4408f9f7ff9518d4f87308/tenor.gif?itemid=8199739",
		"https://media1.tenor.com/images/7443eb36be27659fc4d3effbaa766db5/tenor.gif?itemid=11358249",
		"https://media1.tenor.com/images/e69ebde3631408c200777ebe10f84367/tenor.gif?itemid=5081296",
		"https://media1.tenor.com/images/f5ec64b40d2adf7deb84e3c0e192ff32/tenor.gif?itemid=6194053",
		"https://media1.tenor.com/images/4b5e9867209d7b1712607958e01a80f1/tenor.gif?itemid=5298257",
		"https://media1.tenor.com/images/d5668af606ca4d0332a6507418cabbce/tenor.gif?itemid=4952249",
		"https://media1.tenor.com/images/0436bfc9861b4b57ffffda82d3adad6e/tenor.gif?itemid=15550145",
		"https://media1.tenor.com/images/213ec50caaf02d27d358363016204d1d/tenor.gif?itemid=4553386",
		"https://media1.tenor.com/images/2e46dd93246532cda451359a4aeb68e7/tenor.gif?itemid=16477983",
		]
		cry.set_image(url = random.choice(cry_gif))
		await ctx.send(embed = cry)

	@command(brief = "Action/Emote command.", aliases = ["triggered",])
	# @is_owner()
	async def angry(self, ctx):
		angry = Embed(
			description = f"{ctx.author.mention} is triggered!",
			color = (0xa451d8)
		)
		angry_gif = [              #20
		"https://media1.tenor.com/images/264117db07e29e3569e29320a8d779ad/tenor.gif?itemid=8880636",
		"https://media1.tenor.com/images/cfbc067a1445d5baa5ca36cc2642a6c4/tenor.gif?itemid=5664724",
		"https://media1.tenor.com/images/386fb4996e952415422e4de3f7ff9273/tenor.gif?itemid=6209492",
		"https://media1.tenor.com/images/1c8acf14af9e107ba14834835f5b4f59/tenor.gif?itemid=12346823",
		"https://media1.tenor.com/images/2f198dc24f638fc9f16776c8ebd183fd/tenor.gif?itemid=14682313",
		"https://media1.tenor.com/images/52560e044056cd971892506ce85eb987/tenor.gif?itemid=4436406",
		"https://media1.tenor.com/images/1eada8b2466daadaeada0d13061eef7f/tenor.gif?itemid=14086662",
		"https://media1.tenor.com/images/6884c2aee4a1036465f8984aa52c9664/tenor.gif?itemid=5254221",
		"https://media1.tenor.com/images/ab175515c664b5777601348e03d67acb/tenor.gif?itemid=16825828",
		"https://media1.tenor.com/images/daecfdbc7a443a83586a7ca2516816a7/tenor.gif?itemid=8453300",
		"https://media1.tenor.com/images/f8ce8a3d9e831a3136aafec10f40e3ce/tenor.gif?itemid=9161940",
		"https://media1.tenor.com/images/68bdb7f778cf76bfaa256ebf53164558/tenor.gif?itemid=5591675",
		"https://media1.tenor.com/images/ff34179bd998761db14fd0bdccdc9efa/tenor.gif?itemid=16408483",
		"https://media1.tenor.com/images/b11e32ec61934d7938b5360da3478671/tenor.gif?itemid=9838777",
		"https://media1.tenor.com/images/d27c7d3ce2a5524d1d9b2683369a32f8/tenor.gif?itemid=10935186",
		"https://media1.tenor.com/images/cb871efa727558862700f8f3f924df67/tenor.gif?itemid=5178234",
		"https://media1.tenor.com/images/856ceaea3e84561af61e0ee20c914b65/tenor.gif?itemid=10528179",
		"https://media1.tenor.com/images/1a12f9c0fea9a4275dfc3b91078b93f9/tenor.gif?itemid=7885199",
		"https://media1.tenor.com/images/036dd881d75355855932fe3273c3dce9/tenor.gif?itemid=13300660",
		"https://media1.tenor.com/images/f3ba0e0e978e4e29e8405b04fa1d3047/tenor.gif?itemid=12565006",
		"https://media1.tenor.com/images/ce9aed75d40e0bb50bdcd4428b0e5cf4/tenor.gif?itemid=8045782",
		]
		angry.set_image(url = random.choice(angry_gif))
		await ctx.send(embed = angry)

	@command(brief = "Action/Emote command.", aliases = ["bored",])
	# @is_owner()
	async def sleepy(self, ctx):
		sleepy = Embed(
			description = f"{ctx.author.mention} is sleepy. *Yawn*",
			color = (0xa451d8)
		)
		sleepy_gif = [                #21
		"https://media1.tenor.com/images/01a41c256bfa30efb34d04af259f4c76/tenor.gif?itemid=18483577",  
		"https://media1.tenor.com/images/46cf8801a50fe43770acaf78ef760c64/tenor.gif?itemid=11627087",
		"https://media1.tenor.com/images/3157a49464f04af4b7669987ede71282/tenor.gif?itemid=11006226",
		"https://media1.tenor.com/images/5a519ab7fbf494265b7ba09de84b05aa/tenor.gif?itemid=12069369",
		"https://media1.tenor.com/images/5a519ab7fbf494265b7ba09de84b05aa/tenor.gif?itemid=12069369",
		"https://media1.tenor.com/images/51612fc78b9dae95497aa78997e077bb/tenor.gif?itemid=5959873",
		"https://media1.tenor.com/images/52bf1afef19876cdaec8906952254802/tenor.gif?itemid=12348565",
		"https://media1.tenor.com/images/62299afcedd465b631f9baa9786bd83b/tenor.gif?itemid=6238156",
		"https://media1.tenor.com/images/fcb5ce928c4dfb8dd416a97b260cbe9a/tenor.gif?itemid=4874925",
		"https://media1.tenor.com/images/58a9f04be8cb7bef740476f464a2d83d/tenor.gif?itemid=12003890",
		"https://media1.tenor.com/images/6b1d8cf7b9880bcfea290eea918b16fc/tenor.gif?itemid=5948549",
		"https://media1.tenor.com/images/0057a860ca346c44cbf0efdfd8b15eb0/tenor.gif?itemid=14086687",
		"https://media1.tenor.com/images/9cef52ce27ab97e0fa9cfac1cdc1007f/tenor.gif?itemid=9525859",
		"https://media1.tenor.com/images/afea90ea513137a2b7d94bea824830a5/tenor.gif?itemid=16026798",
		"https://media1.tenor.com/images/5af92174cdea45848e23841a4c297d7f/tenor.gif?itemid=18671239",
		"https://media1.tenor.com/images/c1e7b7250083d3853355983b52b171a9/tenor.gif?itemid=5888776",
		"https://media1.tenor.com/images/67899e4ce154518e656cb2337b180de0/tenor.gif?itemid=7329024",
		"https://media1.tenor.com/images/078c70e3ed147f6f004773b6640936d7/tenor.gif?itemid=5740828",
		"https://media1.tenor.com/images/18e9f3de7527b810963627f1398ba345/tenor.gif?itemid=15844185",
		"https://media1.tenor.com/images/5d686b3d62e2b948ffa6c83041c8c929/tenor.gif?itemid=14088496",
		"https://media1.tenor.com/images/7dc9941d464271d69c9ea14ea92afc07/tenor.gif?itemid=16514747",
		]
		sleepy.set_image(url = random.choice(sleepy_gif))
		await ctx.send(embed = sleepy)

	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def lewd(self, ctx):
		lewd = Embed(
			description = f"LEWD!!! >_<",
			color = (0xa451d8)
		)
		lewd_gif = [              #20
		"https://media1.tenor.com/images/c118281cf06513a78e2fdc731db48c1b/tenor.gif?itemid=12942783",  
		"https://media1.tenor.com/images/4c03573f06a1bd8841976abdafd16d26/tenor.gif?itemid=15711893",
		"https://media1.tenor.com/images/8f76f034ccc458bd09675c0380f59cb7/tenor.gif?itemid=5634589",
		"https://media1.tenor.com/images/29ab83ef501b53273cdb9489819225ff/tenor.gif?itemid=5522297",
		"https://media1.tenor.com/images/9af8d8afab3b509a97f2440562845682/tenor.gif?itemid=13978385",
		"https://media1.tenor.com/images/fc6b82c2c8c045a0b1e6fc91294292c5/tenor.gif?itemid=6215889",
		"https://media1.tenor.com/images/71015cf10d2bc6ddc6c2dd0d7b294277/tenor.gif?itemid=9096269",
		"https://media1.tenor.com/images/6069f7010fed86cb2105ea02e92129fe/tenor.gif?itemid=16142279",
		"https://media1.tenor.com/images/d9b08d9984e694111ba7107c198f85b7/tenor.gif?itemid=5634600",
		"https://media1.tenor.com/images/f620797a6e17d4fd42108128e3ec2739/tenor.gif?itemid=14885739",
		"https://cdn.weeb.sh/images/Hk-Vz8QPb.gif",
		"https://media1.tenor.com/images/6fb2bb2333394363ca036821eefeef9c/tenor.gif?itemid=11970001",
		"https://media1.tenor.com/images/bc2810fc980244dfe6b3f0993eb70486/tenor.gif?itemid=13984951",
		"https://media1.tenor.com/images/623530b7ab746b12f3f55dc3ed7e78b1/tenor.gif?itemid=20182275",
		"https://media1.tenor.com/images/57cea63fc69039d2e87dc79a770d113a/tenor.gif?itemid=13998416",
		"https://media1.tenor.com/images/3160ca92ab4b8b010c88e53b6461e771/tenor.gif?itemid=7407062",
		"https://media1.tenor.com/images/457705c2534ca05dd0af465c1669e59c/tenor.gif?itemid=9291343",
		"https://media1.tenor.com/images/2a3a020417deca849d7cb6218edf75fa/tenor.gif?itemid=8680310",
		"https://media1.tenor.com/images/d2093fbd1ca78d4bbbd2aa2ed6735866/tenor.gif?itemid=4389460",
		"https://media1.tenor.com/images/114e0924c4cf1e551424e96f174f2498/tenor.gif?itemid=10427730",
		"https://media1.tenor.com/images/a79f6132b7fa7377e3fdd53e6cacb1d7/tenor.gif?itemid=14099744",
		]
		lewd.set_image(url = random.choice(lewd_gif))
		await ctx.send(embed = lewd)

	@command(brief = "Action/Emote command.")
	# @is_owner()
	async def pout(self, ctx):
		pout = Embed(
			description = f"{ctx.author.mention} is pouting. How cute!",
			color = (0xa451d8)
		)
		pout_gif = [            #30
		"https://media1.tenor.com/images/e56e1ae197ea11668756e6e82407e5c5/tenor.gif?itemid=12679335",
		"https://media1.tenor.com/images/66c32f7c84340c36ab34ea8911e81b2f/tenor.gif?itemid=14108774",
		"https://media1.tenor.com/images/bdae8325142ead44983e172edd74c75f/tenor.gif?itemid=10081825",
		"https://media1.tenor.com/images/a2cde795512dffb7ed89448a14d7e68e/tenor.gif?itemid=12007445",
		"https://media1.tenor.com/images/c7870c89c7825232565b41c0104555ab/tenor.gif?itemid=13896033",
		"https://media1.tenor.com/images/3424df822494d78bc184aae3e14d84e3/tenor.gif?itemid=4675166",
		"https://media1.tenor.com/images/8edb176f0430ed576ad2959760a8e98a/tenor.gif?itemid=14274438",
		"https://media1.tenor.com/images/d2ffc7bd132676032e6518fa330d6a2b/tenor.gif?itemid=3567101",
		"https://media1.tenor.com/images/4560e9432b50c125b85d6330e5061f66/tenor.gif?itemid=19062536",
		"https://media1.tenor.com/images/b7e132fd3f4e110ea54ef8aa8f4eebbe/tenor.gif?itemid=15650605",
		"https://media1.tenor.com/images/271668b1037633d7f7ae63dc1a1c29f2/tenor.gif?itemid=14739721",
		"https://media1.tenor.com/images/82cd3636b6e6efebe54059a54b92b720/tenor.gif?itemid=17549065",
		"https://media1.tenor.com/images/244d7a2ca77493a46a8d745e1b3f128a/tenor.gif?itemid=16954069",
		"https://media1.tenor.com/images/2e827ee406ae8c8ba98bcd4236e28b57/tenor.gif?itemid=15411808",
		"https://media1.tenor.com/images/76081e508f20ac1525d1a6ee495869c6/tenor.gif?itemid=13659109",
		"https://media1.tenor.com/images/8d302a8c769e39cb94e2018595bd4834/tenor.gif?itemid=15104654",
		"https://media1.tenor.com/images/3088ccd8b567a915e957b70cf9bbec17/tenor.gif?itemid=11836890",
		"https://media1.tenor.com/images/0b6ab859480cee975647852d2e4d6eb5/tenor.gif?itemid=14666598",
		"https://media1.tenor.com/images/c8bf65854104f13e8e2cdc9453c5222f/tenor.gif?itemid=8687045",
		"https://media1.tenor.com/images/3926887aacdc7126d89f1ea62e165692/tenor.gif?itemid=13632757",
		"https://media1.tenor.com/images/58a26a738703565f7fc276aedabfcfb3/tenor.gif?itemid=5754157",
		"https://media1.tenor.com/images/e6790cbd06722d34644311d5b9425864/tenor.gif?itemid=19966189",
		"https://media1.tenor.com/images/a0dc4b7d23b063c02c4b7076b07412b4/tenor.gif?itemid=17901380",
		"https://media1.tenor.com/images/f9eecb39244e76c0a098f8ab8f6d00f1/tenor.gif?itemid=17382934",
		"https://media1.tenor.com/images/d52117b1bbec0fa89baa8095e2c0fe87/tenor.gif?itemid=11686117",
		"https://media1.tenor.com/images/674da0a4ab3052056313d3cb79ab021a/tenor.gif?itemid=5960636",
		"https://media1.tenor.com/images/52bcf0a1f2c972c46ca322549a1e62b4/tenor.gif?itemid=11836883",
		"https://media1.tenor.com/images/df03f2f28e267792e5074bf31f9a0ef3/tenor.gif?itemid=13354213",
		"https://media1.tenor.com/images/3ea7b9f018307d99cb8d1eada8c8cdd3/tenor.gif?itemid=5960653",
		"https://media1.tenor.com/images/d9f9d99b73d599112ceabb0c71eb3185/tenor.gif?itemid=19383389",
		]
		pout.set_image(url = random.choice(pout_gif))
		await ctx.send(embed = pout)

def setup(bot):
	bot.add_cog(Emotes(bot))

