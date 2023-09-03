from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands import NotOwner
from discord import Member, Embed
from discord import Intents
from discord.ext.commands import is_owner
from discord.ext.commands import MissingRequiredArgument
import random
from typing import Optional
import re
import discord
from discord.ext import commands

class Nova_Emotes(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.sayuri = "<@799047693388742706>"

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("nova_emotes")

	@command(brief = "Action/Emote command.")
	@is_owner()
	async def spank(self, ctx, member: Member, *, message: Optional[str]):
		if member == ctx.author:
			await ctx.send(f"{ctx.author.display_name} wants some spanking.")		
		elif not message:
			if member == ctx.me:
				spank = Embed(
					description = f"{ctx.author.mention} spanks {member.mention}.",
					color = (0xa451d8)
				)
				spank_gif = [                          #10
				"https://media1.tenor.com/images/ef5f040254c2fbf91232088b91fe2341/tenor.gif?itemid=13569259",
				"https://media1.tenor.com/images/2eb222b142f24be14ea2da5c84a92b08/tenor.gif?itemid=15905904",
				"https://media1.tenor.com/images/b51750728709353206263f0407f0be96/tenor.gif?itemid=16173937",
				"https://media1.tenor.com/images/1ffbabd05e0be468f035680111da8325/tenor.gif?itemid=18714058",
				"https://media1.tenor.com/images/a9b8bd2060d76ec286ec8b4c61ec1f5a/tenor.gif?itemid=17784858",
				"https://media1.tenor.com/images/a7ed1e6575b047ae219c8bdef3cdb799/tenor.gif?itemid=16082139",
				"https://media1.tenor.com/images/6b3dda2e995a02ad50ae788a16bfbd64/tenor.gif?itemid=12325914",
				"https://media1.tenor.com/images/59282627be1efaa4baa82193ca371425/tenor.gif?itemid=17299734",
				"https://media1.tenor.com/images/0d202a5b98b413a88a4611feae8cd855/tenor.gif?itemid=16910479",
				"https://media1.tenor.com/images/70914dd178c949c9f6d887ef3c1f1da4/tenor.gif?itemid=4517373",
				"https://media1.tenor.com/images/d94be9c942b034e4a00a66d1e277ba84/tenor.gif?itemid=14179592",
				"https://media1.tenor.com/images/728496977dca8b4afbc31de587495b03/tenor.gif?itemid=14179589",
				"https://media1.tenor.com/images/49cc731f0d76650a83351618b495805b/tenor.gif?itemid=12185289",
				]
				spank.set_image(url = random.choice(spank_gif))
				spank.set_footer(text = "ₕₐᵣ𝒹ₑᵣ 𝒹ₐ𝒹𝒹ᵧ", icon_url = ctx.me.avatar_url)
				await ctx.send(embed = spank)

			else:
				spank = Embed(
					description = f"{ctx.author.mention} spanks {member.mention}. ₛₚₐₙₖ ₘₑ ₛₒₘₑₜᵢₘₑ ₙₒᵥₐ₋ₖᵤₙ",
					color = (0xa451d8)
				)
				spank_gif = [                          #10
				"https://media1.tenor.com/images/ef5f040254c2fbf91232088b91fe2341/tenor.gif?itemid=13569259",
				"https://media1.tenor.com/images/2eb222b142f24be14ea2da5c84a92b08/tenor.gif?itemid=15905904",
				"https://media1.tenor.com/images/b51750728709353206263f0407f0be96/tenor.gif?itemid=16173937",
				"https://media1.tenor.com/images/1ffbabd05e0be468f035680111da8325/tenor.gif?itemid=18714058",
				"https://media1.tenor.com/images/a9b8bd2060d76ec286ec8b4c61ec1f5a/tenor.gif?itemid=17784858",
				"https://media1.tenor.com/images/a7ed1e6575b047ae219c8bdef3cdb799/tenor.gif?itemid=16082139",
				"https://media1.tenor.com/images/6b3dda2e995a02ad50ae788a16bfbd64/tenor.gif?itemid=12325914",
				"https://media1.tenor.com/images/59282627be1efaa4baa82193ca371425/tenor.gif?itemid=17299734",
				"https://media1.tenor.com/images/0d202a5b98b413a88a4611feae8cd855/tenor.gif?itemid=16910479",
				"https://media1.tenor.com/images/70914dd178c949c9f6d887ef3c1f1da4/tenor.gif?itemid=4517373",
				"https://media1.tenor.com/images/d94be9c942b034e4a00a66d1e277ba84/tenor.gif?itemid=14179592",
				"https://media1.tenor.com/images/728496977dca8b4afbc31de587495b03/tenor.gif?itemid=14179589",
				"https://media1.tenor.com/images/49cc731f0d76650a83351618b495805b/tenor.gif?itemid=12185289",
				]
				spank.set_image(url = random.choice(spank_gif))
				await ctx.send(embed = spank)	

		else:
			spank = Embed(
				description = message,
				color = (0xa451d8)
			)
			spank_gif = [                          #10
			"https://media1.tenor.com/images/ef5f040254c2fbf91232088b91fe2341/tenor.gif?itemid=13569259",
			"https://media1.tenor.com/images/2eb222b142f24be14ea2da5c84a92b08/tenor.gif?itemid=15905904",
			"https://media1.tenor.com/images/b51750728709353206263f0407f0be96/tenor.gif?itemid=16173937",
			"https://media1.tenor.com/images/1ffbabd05e0be468f035680111da8325/tenor.gif?itemid=18714058",
			"https://media1.tenor.com/images/a9b8bd2060d76ec286ec8b4c61ec1f5a/tenor.gif?itemid=17784858",
			"https://media1.tenor.com/images/a7ed1e6575b047ae219c8bdef3cdb799/tenor.gif?itemid=16082139",
			"https://media1.tenor.com/images/6b3dda2e995a02ad50ae788a16bfbd64/tenor.gif?itemid=12325914",
			"https://media1.tenor.com/images/59282627be1efaa4baa82193ca371425/tenor.gif?itemid=17299734",
			"https://media1.tenor.com/images/0d202a5b98b413a88a4611feae8cd855/tenor.gif?itemid=16910479",
			"https://media1.tenor.com/images/70914dd178c949c9f6d887ef3c1f1da4/tenor.gif?itemid=4517373",
			"https://media1.tenor.com/images/d94be9c942b034e4a00a66d1e277ba84/tenor.gif?itemid=14179592",
			"https://media1.tenor.com/images/728496977dca8b4afbc31de587495b03/tenor.gif?itemid=14179589",
			"https://media1.tenor.com/images/49cc731f0d76650a83351618b495805b/tenor.gif?itemid=12185289",
			]
			spank.set_image(url = random.choice(spank_gif))
			await ctx.send(embed = spank)

	@spank.error
	async def spank_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.")
	@is_owner()
	async def salute(self, ctx, member: Member, *, message: Optional[str]):
		if member == ctx.author:
			await ctx.send(f"How does that even work {ctx.author.display_name}?")		
		elif not message:
			salute = Embed(
				description = f"{member.mention}, {ctx.author.mention} salutes you.",
				color = (0xa451d8)
			)
			salute_gif = [                #20
			"https://media1.tenor.com/images/02c955aea4cb209e8db99c4d740324ae/tenor.gif?itemid=17221576",
			"https://media1.tenor.com/images/f821ff1a4a904d03000e08ca657233a5/tenor.gif?itemid=5359089",
			"https://media1.tenor.com/images/de6d3c7959c2a0629900b16ee83e3982/tenor.gif?itemid=14340477",
			"https://media1.tenor.com/images/0a00063e3932768b1c13454e6669bd7e/tenor.gif?itemid=19736169",
			"https://media1.tenor.com/images/93fc25c6157ace69995f7d3790ff77a2/tenor.gif?itemid=17226659",
			"https://media1.tenor.com/images/2d6ff2c8df840be0d40453c054257ecd/tenor.gif?itemid=12003911",
			"https://media1.tenor.com/images/7491c660fdeb41b5fe36dcdceefbab81/tenor.gif?itemid=15328106",
			"https://media1.tenor.com/images/cd96418735156690273ab1f82dcdb479/tenor.gif?itemid=19850530",
			"https://media1.tenor.com/images/b9ff42f01e9986554f7e4d0f3f48342a/tenor.gif?itemid=14132786",
			"https://media1.tenor.com/images/baa2e44e0358009a8dadb8c5b7eb86d9/tenor.gif?itemid=17435840",
			"https://media1.tenor.com/images/beb2b4984adde75060fcbea7882f383f/tenor.gif?itemid=13582058",
			"https://media1.tenor.com/images/acef6823bc1994bd13c1e8d8dc59bf14/tenor.gif?itemid=17483155",
			"https://media1.tenor.com/images/f2a821152c6484d2b494d867a558dc4f/tenor.gif?itemid=14328271",
			"https://media1.tenor.com/images/bf3c2829bb29e1adaaf797be211d1e11/tenor.gif?itemid=15102447",
			"https://media1.tenor.com/images/dac64d22b7d36b93a638c1b17fd8430a/tenor.gif?itemid=5192849",
			"https://media1.tenor.com/images/cdcc36280181a3d1e749c8af05c13e9f/tenor.gif?itemid=16915641",
			"https://media1.tenor.com/images/955a2f31e83feb0ff7623ca77b3f5099/tenor.gif?itemid=19964475",
			"https://media1.tenor.com/images/84875d46ee0cfea33cff1a3549302a5a/tenor.gif?itemid=20829881",
			"https://media1.tenor.com/images/bde6266b1d73110864ee9997e83e2cb9/tenor.gif?itemid=20643489",
			"https://media1.tenor.com/images/c7ce49839afb1732f13d1ac6e7a37bc4/tenor.gif?itemid=6083454",
			]
			salute.set_image(url = random.choice(salute_gif))
			await ctx.send(embed = salute)
		else:
			salute = Embed(
				description = message,
				color = (0xa451d8)
			)
			salute_gif = [                #20
			"https://media1.tenor.com/images/02c955aea4cb209e8db99c4d740324ae/tenor.gif?itemid=17221576",
			"https://media1.tenor.com/images/f821ff1a4a904d03000e08ca657233a5/tenor.gif?itemid=5359089",
			"https://media1.tenor.com/images/de6d3c7959c2a0629900b16ee83e3982/tenor.gif?itemid=14340477",
			"https://media1.tenor.com/images/0a00063e3932768b1c13454e6669bd7e/tenor.gif?itemid=19736169",
			"https://media1.tenor.com/images/93fc25c6157ace69995f7d3790ff77a2/tenor.gif?itemid=17226659",
			"https://media1.tenor.com/images/2d6ff2c8df840be0d40453c054257ecd/tenor.gif?itemid=12003911",
			"https://media1.tenor.com/images/7491c660fdeb41b5fe36dcdceefbab81/tenor.gif?itemid=15328106",
			"https://media1.tenor.com/images/cd96418735156690273ab1f82dcdb479/tenor.gif?itemid=19850530",
			"https://media1.tenor.com/images/b9ff42f01e9986554f7e4d0f3f48342a/tenor.gif?itemid=14132786",
			"https://media1.tenor.com/images/baa2e44e0358009a8dadb8c5b7eb86d9/tenor.gif?itemid=17435840",
			"https://media1.tenor.com/images/beb2b4984adde75060fcbea7882f383f/tenor.gif?itemid=13582058",
			"https://media1.tenor.com/images/acef6823bc1994bd13c1e8d8dc59bf14/tenor.gif?itemid=17483155",
			"https://media1.tenor.com/images/f2a821152c6484d2b494d867a558dc4f/tenor.gif?itemid=14328271",
			"https://media1.tenor.com/images/bf3c2829bb29e1adaaf797be211d1e11/tenor.gif?itemid=15102447",
			"https://media1.tenor.com/images/dac64d22b7d36b93a638c1b17fd8430a/tenor.gif?itemid=5192849",
			"https://media1.tenor.com/images/cdcc36280181a3d1e749c8af05c13e9f/tenor.gif?itemid=16915641",
			"https://media1.tenor.com/images/955a2f31e83feb0ff7623ca77b3f5099/tenor.gif?itemid=19964475",
			"https://media1.tenor.com/images/84875d46ee0cfea33cff1a3549302a5a/tenor.gif?itemid=20829881",
			"https://media1.tenor.com/images/bde6266b1d73110864ee9997e83e2cb9/tenor.gif?itemid=20643489",
			"https://media1.tenor.com/images/c7ce49839afb1732f13d1ac6e7a37bc4/tenor.gif?itemid=6083454",
			]
			salute.set_image(url = random.choice(salute_gif))
			await ctx.send(embed = salute)

	@salute.error
	async def salute_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.")
	@is_owner()
	async def fistbump(self, ctx, member: Member, *, message: Optional[str]):
		if member == ctx.author:
			await ctx.send(f"How does that even work {ctx.author.display_name}?")		
		elif not message:
			fistbump = Embed(
				description = f"{member.mention}, {ctx.author.mention} fistbumps with you.",
				color = (0xa451d8)
			)
			fistbump_gif = [         #15      
			"https://media1.tenor.com/images/23e26d7096f470ddcf80c84299c34e40/tenor.gif?itemid=14285305",
			"https://media1.tenor.com/images/eeda515e9e23604a46565ae7ff90dfb4/tenor.gif?itemid=10380419",
			"https://media1.tenor.com/images/a4a271d3ccc6eb35c45c65ddad461dd2/tenor.gif?itemid=17376223",
			"https://media1.tenor.com/images/8e29e9ef91041d68d89a4f607f4530f9/tenor.gif?itemid=16312890",
			"https://media1.tenor.com/images/6bd921415f5a22ccd5d5d77613c92b3e/tenor.gif?itemid=5076745",
			"https://media1.tenor.com/images/5627e0deaa5ce4ee872712a2718353c9/tenor.gif?itemid=4931152",
			"https://media1.tenor.com/images/4336c5606ad7fb7ae553c96c87a3adc7/tenor.gif?itemid=14531455",
			"https://media1.tenor.com/images/ab9aff21ab4d16fbf5922e4dd7dc5673/tenor.gif?itemid=14828411",
			"https://media1.tenor.com/images/ace399cf2968b4dea77a8f1cc684c5cf/tenor.gif?itemid=11743559",
			"https://media1.tenor.com/images/d6c393135b555225e418a16f38ffda0f/tenor.gif?itemid=16146439",
			"https://media1.tenor.com/images/f2b1abdf459a77e743b5b3c4d4c1fd56/tenor.gif?itemid=17940812",
			"https://media1.tenor.com/images/383c325dba81ecb3d52350dab1f95e13/tenor.gif?itemid=20338299",
			"https://media1.tenor.com/images/584473553d869a01572c0d3cd99810fa/tenor.gif?itemid=17742134",
			"https://media1.tenor.com/images/2604566c26d9bda3012c36c3b29357ac/tenor.gif?itemid=18204553",
			"https://media1.tenor.com/images/0bfae47add0180fd93b52ebb8bf89dd4/tenor.gif?itemid=5047789",
			]
			fistbump.set_image(url = random.choice(fistbump_gif))
			await ctx.send(embed = fistbump)
		else:
			fistbump = Embed(
				description = message,
				color = (0xa451d8)
			)
			fistbump_gif = [         #15      
			"https://media1.tenor.com/images/23e26d7096f470ddcf80c84299c34e40/tenor.gif?itemid=14285305",
			"https://media1.tenor.com/images/eeda515e9e23604a46565ae7ff90dfb4/tenor.gif?itemid=10380419",
			"https://media1.tenor.com/images/a4a271d3ccc6eb35c45c65ddad461dd2/tenor.gif?itemid=17376223",
			"https://media1.tenor.com/images/8e29e9ef91041d68d89a4f607f4530f9/tenor.gif?itemid=16312890",
			"https://media1.tenor.com/images/6bd921415f5a22ccd5d5d77613c92b3e/tenor.gif?itemid=5076745",
			"https://media1.tenor.com/images/5627e0deaa5ce4ee872712a2718353c9/tenor.gif?itemid=4931152",
			"https://media1.tenor.com/images/4336c5606ad7fb7ae553c96c87a3adc7/tenor.gif?itemid=14531455",
			"https://media1.tenor.com/images/ab9aff21ab4d16fbf5922e4dd7dc5673/tenor.gif?itemid=14828411",
			"https://media1.tenor.com/images/ace399cf2968b4dea77a8f1cc684c5cf/tenor.gif?itemid=11743559",
			"https://media1.tenor.com/images/d6c393135b555225e418a16f38ffda0f/tenor.gif?itemid=16146439",
			"https://media1.tenor.com/images/f2b1abdf459a77e743b5b3c4d4c1fd56/tenor.gif?itemid=17940812",
			"https://media1.tenor.com/images/383c325dba81ecb3d52350dab1f95e13/tenor.gif?itemid=20338299",
			"https://media1.tenor.com/images/584473553d869a01572c0d3cd99810fa/tenor.gif?itemid=17742134",
			"https://media1.tenor.com/images/2604566c26d9bda3012c36c3b29357ac/tenor.gif?itemid=18204553",
			"https://media1.tenor.com/images/0bfae47add0180fd93b52ebb8bf89dd4/tenor.gif?itemid=5047789",
			]
			fistbump.set_image(url = random.choice(fistbump_gif))
			await ctx.send(embed = fistbump)

	@fistbump.error
	async def fistbump_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")

	@command(brief = "Action/Emote command.", aliases = ["surprised",])
	@is_owner()
	async def shocked(self, ctx):
		shocked = Embed(
			description = f"{ctx.author.mention} is shocked!",
			color = (0xa451d8)
		)
		shocked_gif = [                  #20
		"https://media1.tenor.com/images/82023bd02e34a61401a164fee0679074/tenor.gif?itemid=6091874",
		"https://media1.tenor.com/images/bf1e5ee94ccd13576d3520d60d692317/tenor.gif?itemid=5384592",
		"https://media1.tenor.com/images/dc5664183fca008ae5a92edffe39a03c/tenor.gif?itemid=12921557",
		"https://media1.tenor.com/images/28e2ac30d9c57ddda7dd1942ccda9f1b/tenor.gif?itemid=18880714",
		"https://media1.tenor.com/images/4d34397125a4d5fd64b66935a732fac8/tenor.gif?itemid=6091843",
		"https://media1.tenor.com/images/4d34397125a4d5fd64b66935a732fac8/tenor.gif?itemid=6091843",
		"https://media1.tenor.com/images/cc1f12c1d2f453358d01f89c445feb21/tenor.gif?itemid=6091842",
		"https://media1.tenor.com/images/9265747cd10ebb8146c3b890fed00e11/tenor.gif?itemid=14778758",
		"https://media1.tenor.com/images/9cfbcbedb9f6a646ad64477cf8b02c3b/tenor.gif?itemid=16286974",
		"https://media1.tenor.com/images/f6337ae3cf8f71d89928890e507dac55/tenor.gif?itemid=13963380",
		"https://media1.tenor.com/images/e38a9e8fe558bf48893f4c0069aa2b44/tenor.gif?itemid=5554691",
		"https://media1.tenor.com/images/febdcf035d8d369ef86158dff97080b2/tenor.gif?itemid=14088533",
		"https://media1.tenor.com/images/05c0dc9ec968a480bcd617302b8980c1/tenor.gif?itemid=10537518",
		"https://media1.tenor.com/images/dff48ef5e9d349d51a00cbc100b544f8/tenor.gif?itemid=16584562",
		"https://media1.tenor.com/images/3711bc77009d38cd9eaac6eb7cf0ebfe/tenor.gif?itemid=13843229",
		"https://media1.tenor.com/images/4b3dce62027ea94154c3eab0469938f1/tenor.gif?itemid=14172292",
		"https://media1.tenor.com/images/a067120f8abc11cfe98f767d5e12b73c/tenor.gif?itemid=8539535",
		"https://media1.tenor.com/images/4f97335019ce18693216ad3933197d33/tenor.gif?itemid=16780297",
		"https://media1.tenor.com/images/7257bee0931da35589329205d77f5a91/tenor.gif?itemid=4556193",
		"https://media1.tenor.com/images/42baa03499a997cae6216867f0033409/tenor.gif?itemid=13893147",
		]
		shocked.set_image(url = random.choice(shocked_gif))
		await ctx.send(embed = shocked)

	@command(brief = "Action/Emote command.", aliases = ["cya", "bye", "later", "laters", "ciao"])
	@is_owner()
	async def wave(self, ctx):
		wave = Embed(
			description = f"{ctx.author.mention} waves you a goodbye.",
			color = (0xa451d8)
		)
		wave_gif = [                #25
		"https://media1.tenor.com/images/943a3f95936d66dc0c78fd445893431e/tenor.gif?itemid=9060940",
		"https://media1.tenor.com/images/d6a2910107681d5d2deabf0b4d872906/tenor.gif?itemid=10548215",
		"https://media1.tenor.com/images/c0d3b9080d788636a4122f1665f46a52/tenor.gif?itemid=17085889",
		"https://media1.tenor.com/images/f82fdfe817cfb8dacb5bd5c7dadb632d/tenor.gif?itemid=8718221",
		"https://media1.tenor.com/images/33fdd8dc7564b56d5905428484f5aee4/tenor.gif?itemid=5604313",
		"https://media1.tenor.com/images/8a87452b39aa0a394f19b42d8d2e790d/tenor.gif?itemid=12284917",
		"https://media1.tenor.com/images/86a81a4a4e63afc759800f452b396787/tenor.gif?itemid=15151699",
		"https://media1.tenor.com/images/49b1aa90b1a0b63ee3a89a651efdcd01/tenor.gif?itemid=14596996",
		"https://media1.tenor.com/images/8b00c464465b4ad9ead8db11ccdbdba2/tenor.gif?itemid=9905373",
		"https://media1.tenor.com/images/31f8ab4eab53b09da67b0216c4f8835e/tenor.gif?itemid=17120141",
		"https://media1.tenor.com/images/56976dab54f0f14b5d9b87d100091858/tenor.gif?itemid=17441907",
		"https://media1.tenor.com/images/8bbf9194008e3f8f2f2665c2cbe8dbca/tenor.gif?itemid=10837648",
		"https://media1.tenor.com/images/72c9b849aa10b222371ebb99a6b1896a/tenor.gif?itemid=8807701",
		"https://media1.tenor.com/images/c2e21a9d8e17c1d335166dbcbe0bd1bf/tenor.gif?itemid=5459102",
		"https://media1.tenor.com/images/538825f8bd7e421ac1103b5e7d878138/tenor.gif?itemid=15875040",
		"https://media1.tenor.com/images/e66e164e6540ed204fce8cb4cb0c3037/tenor.gif?itemid=17416714",
		"https://media1.tenor.com/images/2b121b915c9f3411eeba5092cd3c80bb/tenor.gif?itemid=13783216",
		"https://media1.tenor.com/images/a2a85146f3ea210a8e5f8e4042d96f16/tenor.gif?itemid=5142331",
		"https://media1.tenor.com/images/d2a4bcd7648c32d1a10c36b918b45c6b/tenor.gif?itemid=14518602",
		"https://media1.tenor.com/images/fc2301f7b21a8088d2b2a681e12d4ab1/tenor.gif?itemid=16387072",
		"https://media1.tenor.com/images/cb19d14edb62e4d38ebba1cb85398526/tenor.gif?itemid=19148104",
		"https://media1.tenor.com/images/e71dc0a3b0ed41dd570bd9214705ec04/tenor.gif?itemid=20884329",
		"https://media1.tenor.com/images/31510c03beffc40d02cb25374fd3f482/tenor.gif?itemid=16699823",
		"https://media1.tenor.com/images/79f33c2f524cbfed4ef6896b39e67663/tenor.gif?itemid=9416181",
		"https://media1.tenor.com/images/f5cd33863e8319ea72990eefc8e697a8/tenor.gif?itemid=5417197",
		]
		wave.set_image(url = random.choice(wave_gif))
		await ctx.send(embed = wave)

	@command(brief = "Action/Emote command.")
	@is_owner()
	async def wink(self, ctx):
		wink = Embed(
			description = f"{ctx.author.mention} gives a wink.",
			color = (0xa451d8)
		)
		wink_gif = [                      #25
		"https://media1.tenor.com/images/d5b51570f8301f588eeb5565c7f110f8/tenor.gif?itemid=18043249",
		"https://media1.tenor.com/images/c554aac83978470c0680543107af4b6d/tenor.gif?itemid=12244993",
		"https://media1.tenor.com/images/0ff40f36fb5c079713ad724f306318ec/tenor.gif?itemid=8030025",
		"https://media1.tenor.com/images/922399d5cae85e03fccefcdd0f7bef59/tenor.gif?itemid=5316207",
		"https://media1.tenor.com/images/02c4eafb14ad8ed84f4fd92b1a02cbed/tenor.gif?itemid=10081698",
		"https://media1.tenor.com/images/3c192c5ee89c5645d882efe704ef29cf/tenor.gif?itemid=14132778",
		"https://media1.tenor.com/images/61efdb0459289dda96a3871f4f575987/tenor.gif?itemid=12188360",
		"https://media1.tenor.com/images/753abb3578ec83e9a7afc297725e6140/tenor.gif?itemid=16282623",
		"https://media1.tenor.com/images/5bbfe72d3faca25bdac64d85442ff553/tenor.gif?itemid=15516760",
		"https://media1.tenor.com/images/d910e620d5956cc60eb8db21fb2beca8/tenor.gif?itemid=14683647",
		"https://media1.tenor.com/images/1c29783da457f0ad3108f3b27798243a/tenor.gif?itemid=5364920",
		"https://media1.tenor.com/images/63e88f91358ff36ae405eee1cb110c2a/tenor.gif?itemid=12381398",
		"https://media1.tenor.com/images/70251734d3ef118512486a0c0836420f/tenor.gif?itemid=16944825",
		"https://media1.tenor.com/images/52324c9221f5ce0dc9edcef3271b4e50/tenor.gif?itemid=15249578",
		"https://media1.tenor.com/images/da85600de68abeaadf9f587d69f5672e/tenor.gif?itemid=16767739",
		"https://media1.tenor.com/images/0fdaa91d1ceca5f3d8b8a7d7102be67f/tenor.gif?itemid=15338280",
		"https://media1.tenor.com/images/bb1a128d84c776c76c60610424bc1f4c/tenor.gif?itemid=15757089",
		"https://media1.tenor.com/images/0c3dab23f55e448f87b66a1f607487a8/tenor.gif?itemid=16357344",
		"https://media1.tenor.com/images/60d3f9266db593acbb5013d21052f07e/tenor.gif?itemid=15061183",
		"https://media1.tenor.com/images/a058e6076f9829d3dd1c728a860ebee4/tenor.gif?itemid=18742623",
		"https://media1.tenor.com/images/f9bafbbcc46ccd124861608446b47e4e/tenor.gif?itemid=19713912",
		"https://media1.tenor.com/images/9c68fcf0495d50200551ca1288c96b33/tenor.gif?itemid=19617620",
		"https://media1.tenor.com/images/7e7d7a6a6084c741804e29b6c46b1b5d/tenor.gif?itemid=12003936",
		"https://media1.tenor.com/images/e6ed8157ce47585bbddc7f933d649f31/tenor.gif?itemid=14325335",
		"https://media1.tenor.com/images/1a3e80b2d8b08e39d3a7355dc23a88db/tenor.gif?itemid=15018586",
		]
		wink.set_image(url = random.choice(wink_gif))
		await ctx.send(embed = wink)

	@command(brief = "Action/Emote command.",)
	@is_owner()
	async def nod(self, ctx):
		nod = Embed(
			description = f"{ctx.author.mention} Uh-huh.",
			color = (0xa451d8)
		)
		nod_gif = [             #20
		"https://media1.tenor.com/images/a3d3d51c8ca4598f2fb39da51ec9584f/tenor.gif?itemid=4361784",
		"https://media1.tenor.com/images/5f58f3bcd3f62390bc94626478b31b82/tenor.gif?itemid=15194868",
		"https://media1.tenor.com/images/f6831eeb7c2ba1984b3e5a41b047f737/tenor.gif?itemid=13451534",
		"https://media1.tenor.com/images/6634220d4c4e0c5da6b4a5cd2ba5a72f/tenor.gif?itemid=15254753",
		"https://media1.tenor.com/images/de65a7bc3e22b2958348696cf597bba9/tenor.gif?itemid=9659282",
		"https://media1.tenor.com/images/9a4c8411e85e144b8c6d16b0c5c3ff73/tenor.gif?itemid=15175750",
		"https://media1.tenor.com/images/5d96b5d2c8b4c5fe288a77d9f1b2097b/tenor.gif?itemid=15974482",
		"https://media1.tenor.com/images/5a23907c439c461573cbc30d7b2c4538/tenor.gif?itemid=16574634",
		"https://media1.tenor.com/images/6eb800a45081b7b994326290f8fccb2a/tenor.gif?itemid=17083387",
		"https://media1.tenor.com/images/b348f0ed63e012af15fb22534fa40201/tenor.gif?itemid=12046342",
		"https://media1.tenor.com/images/bd47e50bf36d32b5e061024fb6f4cfab/tenor.gif?itemid=18757343",
		"https://media1.tenor.com/images/ef2082ab1c2e5d0350cbfbc900166fe7/tenor.gif?itemid=19621826",
		"https://media1.tenor.com/images/83699082893947f87bf4639df98e6e65/tenor.gif?itemid=14159777",
		"https://media1.tenor.com/images/599bb574475255277d9f4b5af5eacd60/tenor.gif?itemid=18520580",
		"https://media1.tenor.com/images/d8c25556c941af73ea2bf5e4f25c905c/tenor.gif?itemid=13138932",
		"https://media1.tenor.com/images/2a2d672820da0311e8a614fcfb302856/tenor.gif?itemid=13451461",
		"https://media1.tenor.com/images/42fba891f5f950f69ab8de1b1f818884/tenor.gif?itemid=20107311",
		"https://media1.tenor.com/images/b2df283fc5c8b4749a9026f6a9bdef82/tenor.gif?itemid=17508542",
		"https://media1.tenor.com/images/2a3a020417deca849d7cb6218edf75fa/tenor.gif?itemid=8680310",
		"https://media1.tenor.com/images/6451a9f11dab2e42940a0e4378987314/tenor.gif?itemid=15115643",
		]
		nod.set_image(url = random.choice(nod_gif))
		await ctx.send(embed = nod)

	@command(brief = "Action/Emote command.", aliases=["smh",])
	@is_owner()
	async def facepalm(self, ctx):
		facepalm = Embed(
			description = f"{ctx.author.mention} *sighs*",
			color = (0xa451d8)
		)
		facepalm_gif = [            #16
		"https://media1.tenor.com/images/bc3f3842afb1edcba095f9bf766405b2/tenor.gif?itemid=17778269",
		"https://media1.tenor.com/images/a29e11bc1132181031ed66ee2a4747fb/tenor.gif?itemid=19368854",
		"https://media1.tenor.com/images/d8d29f0d56957f209f42105baa4e00f1/tenor.gif?itemid=17236628",
		"https://media1.tenor.com/images/142d74bbd13fc305aed5a4894c0c3f7f/tenor.gif?itemid=16642818",
		"https://media1.tenor.com/images/76d2ec47ec76fa36b2fce913331ba7e3/tenor.gif?itemid=5533025",
		"https://media1.tenor.com/images/9a269d284388ae4906983f5dfbb15c64/tenor.gif?itemid=17106384",
		"https://media1.tenor.com/images/015b8063c7018c2880e88c6014a0ffaf/tenor.gif?itemid=12168336",
		"https://media1.tenor.com/images/2e69f243490dedfdfc15c4a9aa52364c/tenor.gif?itemid=15580787",
		"https://media1.tenor.com/images/480cdeb59d3d5d50dd206283a944b8e1/tenor.gif?itemid=16327659",
		"https://media1.tenor.com/images/f70402ebf5e19566ff17a6394ae217ee/tenor.gif?itemid=19147401",
		"https://media1.tenor.com/images/9f970a433ee5204695e487e3076ea46e/tenor.gif?itemid=20554679",
		"https://media1.tenor.com/images/5bbe44f124365864b1537f686d0a77f5/tenor.gif?itemid=20556956",
		"https://media1.tenor.com/images/04ce28c62c8cfeb102b3ac2a9bf28050/tenor.gif?itemid=12411417",
		"https://media1.tenor.com/images/b8e234ac4aa6aa64b582895911de2046/tenor.gif?itemid=12411488",
		"https://media1.tenor.com/images/43f438c58296dabd4bd71f282987f44c/tenor.gif?itemid=10157360",
		"https://media1.tenor.com/images/a316e25a9eb6228d562c191c9138f399/tenor.gif?itemid=14793863",
		]

		facepalm.set_image(url = random.choice(facepalm_gif))
		await ctx.send(embed = facepalm)

	@command(brief = "Action/Emote command.")
	@is_owner()
	async def nosebleed(self, ctx):
	  nosebleed_desc = ["Nova senpai dont look >_<", "Nova senpai you pervert." ]
	  nosebleed = Embed(
	    description = random.choice(nosebleed_desc),
	    colour = (0xa451d8)
	  )
	  nosebleed_gif = [
	  "https://media1.tenor.com/images/9dbd860f873bc8d55770195cd31124a6/tenor.gif?itemid=9411114",
	  "https://media1.tenor.com/images/0d72a7278618f03f91c3f0ff58862b5a/tenor.gif?itemid=13804817",
	  "https://media1.tenor.com/images/385c7b4211ce6b251ef67e6f1737050c/tenor.gif?itemid=8882037",
	  "https://media1.tenor.com/images/9d4d11f65f9faa9ee18ad361aec03adb/tenor.gif?itemid=5966096",
	  "https://media1.tenor.com/images/d743a05d1989e520298db079099faab5/tenor.gif?itemid=16361904",
	  "https://media1.tenor.com/images/c87c323a48385a0dff1a2aaa18aea28d/tenor.gif?itemid=17658635",
	  "https://media1.tenor.com/images/0eca82142481add1ddc8d8b031b91d23/tenor.gif?itemid=5469034",
	]

	  nosebleed.set_image(url = random.choice(nosebleed_gif))
	  await ctx.send(embed = nosebleed)


	@command(brief = "Action/Emote command.")
	@is_owner()
	async def narutogrin(self, ctx):
	  narutogrin = Embed(
	    colour = (0xeb661f)
	  )
	  narutogrin_gif = [
	  "https://media1.tenor.com/images/273c37c56e94765d278aaa7e2f52d887/tenor.gif?itemid=15767589"
	]

	  narutogrin.set_image(url = random.choice(narutogrin_gif))
	  await ctx.send(embed = narutogrin)


	@command(brief = "Action/Emote command.")
	@is_owner()
	async def kiralaugh(self, ctx):
	  kiralaugh = Embed(
	    colour = (0xeb1f1f)
	  )
	  kiralaugh.set_image(url = "https://media1.tenor.com/images/2882a21e8a7175c16efe39e640e28734/tenor.gif?itemid=5812705")
	  await ctx.send(embed = kiralaugh)


	@command(brief = "Action/Emote command.")
	@is_owner()
	async def twats(self, ctx):
	  twats = Embed(
	    description = "THATS WHAT SHE SAID!",
	  )
	  twats.set_image(url = "https://media1.tenor.com/images/9867b1fa3ac337972f761e313a177609/tenor.gif?itemid=4084628")
	  await ctx.send(embed = twats)


	@command(aliases = ["mendokusei"],brief = "Action/Emote command.")
	@is_owner()
	async def troublesome(self, ctx):
	  troublesome_desc = ["*sigh*  this is troublesome.", "*Tsk*  How troublesome...", "Ttaku Mendokusei..."]
	  troublesome = Embed(
	    description = random.choice(troublesome_desc),
	    colour = (0x8f8d8d)
	  )
	  troublesome_gif = [
	  "https://media1.tenor.com/images/eed0ad830dd2e057df7be5cbd7145c2d/tenor.gif?itemid=10868560","https://media1.tenor.com/images/d8d29f0d56957f209f42105baa4e00f1/tenor.gif?itemid=17236628", "https://media1.tenor.com/images/015178d65807d62b87a1e025f68417f4/tenor.gif?itemid=10073110", "https://media1.tenor.com/images/cfd82e8d51f551f620f72b31ad053c6c/tenor.gif?itemid=18556323", "https://media1.tenor.com/images/11430a18119755d6122f5fe9046a60df/tenor.gif?itemid=13199966",
	]

	  troublesome.set_image(url = random.choice(troublesome_gif))
	  await ctx.send(embed = troublesome)


	@command(name = "dambro", aliases = ["damnbro",])
	@is_owner()
	async def dambro(self, ctx):
		dambro = Embed(colour = (0xa451d8))

		dambro.set_image(url = "https://i0.wp.com/humoroutcasts.com/wp-content/uploads/2017/10/dambro.jpg?fit=300%2C171&ssl=1")
		await ctx.send(embed = dambro)


	@command(name = "man of culture", aliases = ["moc", "cultured",])
	@is_owner()
	async def man_of_culture(self, ctx, member: Optional[Member]):

		if member == None:
			man_of_culture_embed = Embed(description = "I see you are a man of culture as well.",
				                         colour = (0xa451d8))

			man_of_culture_embed.set_image(url = "https://media1.tenor.com/images/a5305f4cdbf72af97f456db36a499b06/tenor.gif?itemid=10903367")

			await ctx.send(embed = man_of_culture_embed)

		else:
			man_of_culture_embed = Embed(description = f"{member.mention} I see you are a man of culture as well.",
				                         colour = (0xa451d8))

			man_of_culture_embed.set_image(url = "https://media1.tenor.com/images/a5305f4cdbf72af97f456db36a499b06/tenor.gif?itemid=10903367")

			await ctx.send(embed = man_of_culture_embed)		

def setup(bot):
	bot.add_cog(Nova_Emotes(bot))