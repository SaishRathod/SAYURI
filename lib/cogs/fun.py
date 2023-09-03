import random
from random import choice, randint
from discord import Member, Embed
from discord.errors import HTTPException
from typing import Optional
from aiohttp import request
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown
from discord.ext.commands import BadArgument
from discord.ext.commands import is_owner

class Fun(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("fun")

	@command(name="greetings", aliases=["hi", "hey", "hello"], brief = "I say hello to you.",)
	async def greetings_command(self, ctx):
		await ctx.send(f"{choice(('Hello', 'Hi', 'Hey', 'Hiya'))} {ctx.author.mention}! {choice(('How you doin?', 'How are you today?', 'How you doin today?'))}")

	@command(brief = "Put some text after the command and I'll say it on your behalf. No need to thank me ^^")
	@is_owner()
	async def say(self, ctx, *, message):
		await ctx.message.delete()
		await ctx.send(message)

	@command(aliases = ["8ball", "8b"], brief="Strike up a YES or NO question and I'll tell whether the results are postive or negative. (Good Luck!)")
	async def _8ball(self, ctx, *, question):

		responses = ["It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes – definitely.", "You may rely on it.", "Reply hazy, try again.",
        "Ask again later.", "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."]
		await ctx.channel.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

	# @command(name = "meme", brief = "Summons memes.")
	# @is_owner()
	# async def meme_command(self, ctx):
	# 	meme_url = "https://random-stuff-api.p.rapidapi.com/joke/any"
	# 	querystring = {"api_key":"<REQUIRED>"}
	# 	headers = {
	# 		'x-rapidapi-key': "2cf3bf6845msh6e61bfdbda0bf09p12cecbjsn0025ec727ffa",
	# 		'x-rapidapi-host': "random-stuff-api.p.rapidapi.com"
	# 		}

	# 	async with request("GET", meme_url, headers=headers, params=querystring) as response:
	# 		if response.status == 200:
	# 			data = await response.json()
	# 			meme_image = data["image"]

	# 			meme_embed = Embed(color = (0xa451d8),
	# 					           description = data["caption"])

	# 			meme_embed.set_image(url = meme_image)
	# 			await ctx.send(embed = meme_embed)

	# 		else:
	# 			await ctx.send(f"API sent a {response.status} respose.")

	# @command(name = "pickupline", aliases = ["pl","pickup"])
	# @is_owner()
	# async def pickupline_command(self, ctx):
	# 	pickupline_url = "https://pickupapi.christianabdelmassih.com/api/pickups/"

	# 	async with request("GET", pickupline_url, headers = {}) as response:
	# 		if response.status == 200:
	# 			data = await response.json()

	# 			body = ["body"]

	# 			await ctx.send(f"{body}")

	# 		else:
				# await ctx.send(f"API sent a {response.status} respose.")

	# @command(name = "quote")
	# @is_owner()
	# async def quote_command(self, ctx):
	# 	quote_url = "https://inspirobot.me/api?generate=true"

	# 	async with request("GET", quote_url, headers = {}) as response:
	# 		if response.status == 200:
	# 			data = await response.json()
	# 			# quote_image = data["html"]

	# 			quote_embed = Embed(title = "Here's your quote:",
	# 				                color = (0xa451d8))

	# 			quote_embed.set_image(url = quote_image)

	# 			await ctx.send(data)

	# 		else:
	# 			await ctx.send(f"API sent a {response.status} respose.")

def setup(bot):
	bot.add_cog(Fun(bot))