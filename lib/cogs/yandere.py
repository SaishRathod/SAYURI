from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands import NotOwner, MissingRole
from discord.ext.commands import is_owner, has_role
import random
from discord import Embed
from discord.ext.commands import CheckFailure
from discord.ext.commands import has_permissions, bot_has_permissions, has_role

class Yandere(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("yandere")


	# @command(name = "ily", aliases = ["aishiteru", "143", "ilu",])
	# async def confess(self, ctx):
	# 	if ctx.author.id == 424486126351417344:
	# 		replies = ["I love you too Nova-kun <3", "I love you more Nova-kun.", "ILY2 my love.", "ILY too Nova-kun! ||Wanna hit the dms?||", "143 43.",
	# 		           "01101001 00100000 01101100 01101111 01110110 01100101 00100000 01111001 01101111 01110101 00100000 01110100 01101111 01101111",]
	# 		await ctx.send(f"{random.choice(replies)}")
	# 	else:
	# 		reasons = ["Uh-uh... sorry. I already gave my heart to someone else...", "I am in love with someone else. Please dont bother me.", "Please dont hit on me."]
	# 		await ctx.send(f"{random.choice(reasons)}")

	@command(name = "thanks", aliases = ["thankyou", "thankya"])
	async def thank_command(self, ctx):
		if ctx.author.id == 424486126351417344:
			replies = ["No problem Nova-kun.", "Np, I am always here for you Nova-kun.", "Your welcome ^_^", "Anything for you :heart:"]
			await ctx.send(f"{random.choice(replies)}")
		else:
			reasons = ["No worries ^^"]
			await ctx.send(f"{random.choice(reasons)}")

def setup(bot):
	bot.add_cog(Yandere(bot))