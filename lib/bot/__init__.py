from asyncio import sleep
from datetime import datetime
from glob import glob
from re import search
from discord import Intents
from discord.ext.commands import Cog
from better_profanity import profanity
from discord.errors import HTTPException, Forbidden
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as Botbase
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument, CommandOnCooldown, CheckFailure, MissingPermissions, BotMissingPermissions)
from discord.ext.commands import NotOwner, MissingRole
from discord.ext.commands import Context
from discord.utils import find
from discord import Embed, File, DMChannel
from discord.ext.commands import when_mentioned_or
from discord.ext.commands import command
from discord.ext import commands
import random
import itertools

from ..db import db

profanity.load_censor_words_from_file("./data/profanity.txt")

OWNER_IDS = [424486126351417344]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]
IGNORE_EXCEPTIONS = (CommandNotFound, BadArgument)


def get_prefix(bot, message):
	prefix = db.field("SELECT Prefix FROM guilds WHERE GuildID = ?", message.guild.id)
	prefix = map("".join, itertools.product(*zip(prefix.lower(), prefix.upper())))
	return when_mentioned_or(*prefix)(bot, message)

class Ready(object):
	def __init__(self):
		for cog in COGS:
			setattr(self, cog, False)

	def ready_up(self, cog):
		setattr(self, cog, True)
		print(f"--{cog} cog ready--")

	def all_ready(self):
		return all([getattr(self, cog) for cog in COGS])


class Bot(Botbase):
	def __init__(self):
		self.name = "SAYURI"
		self.cogs_ready = Ready()
		self.ready = False
		self.scheduler = AsyncIOScheduler()
		self.owner = "<@424486126351417344>"
		self.sayuri = "<@799047693388742706>"

		db.autosave(self.scheduler)

		super().__init__(
			command_prefix = get_prefix,
			case_insensitive = True,
			owner_ids = OWNER_IDS, 
			intents = Intents.all()
			)

	def setup(self):
		for cog in COGS:
			self.load_extension(f"lib.cogs.{cog}")
			print(f"--{cog} cog loaded--")

		print("--Setup complete--")

	def update_db(self):
		db.multiexec("INSERT OR IGNORE INTO guilds (GuildID) VALUES (?)",
			         ((guild.id,) for guild in self.guilds))

		db.multiexec("INSERT OR IGNORE INTO welcome (GuildID) VALUES (?)",
			         ((guild.id,) for guild in self.guilds))

		db.multiexec("INSERT OR IGNORE INTO leave (GuildID) VALUES (?)",
			         ((guild.id,) for guild in self.guilds))

		db.multiexec("INSERT OR IGNORE INTO exp (UserID) VALUES (?)",
			         ((member.id,) for member in self.guild.members if not member.bot))

		db.multiexec("INSERT OR IGNORE INTO warnings (UserID) VALUES (?)",
			         ((member.id,) for member in self.guild.members if not member.bot))

		to_remove = []
		stored_members = db.column("SELECT UserID FROM exp")
		for id_ in stored_members:
			if not self.guild.get_member(id_):
				to_remove.append(id_)

		db.multiexec("DELETE FROM exp WHERE UserID = ?",
			         ((id_,) for id_ in to_remove))

		db.multiexec("DELETE FROM warnings WHERE UserID = ?",
			         ((id_,) for id_ in to_remove))

		db.commit()


	def run(self, version):
		self.VERSION = version

		print("Running setup...")
		self.setup()

		with open("./lib/bot/token.0", "r", encoding = "utf-8") as tf:
			self.TOKEN = tf.read()

		print("Sayuri is running...")
		super().run(self.TOKEN, reconnect = True)


	async def on_connect(self):
		print("Sayuri is up.")

	async def on_disconnect(self):
		print("Sayuri disconnected.")

	async def on_error(self, err, *args, **kwargs):
		if err == "on_command_error":
			await args[0].send("Something went wrong.")

			await self.stdout.send("An error occured.")
			raise

	async def on_command_error(self, ctx, exc):
		if any([isinstance(exc, error) for error in IGNORE_EXCEPTIONS]):
			pass
		#elif isinstance(exc.original, HTTPException):
		#	await ctx.send("Unable to send message.")
		elif isinstance(exc, BadArgument):
			pass
		elif isinstance(exc, CommandOnCooldown):
			await ctx.send(f"You are on cooldown. Try again in {exc.retry_after:,.2f} seconds.")
		elif isinstance(exc, NotOwner):                                         
			await ctx.send("Sorry, that command is off-limits to you.")
		elif isinstance(exc, MissingRole):                                      
			await ctx.send("You do not have the required role to execute that command.")
		elif isinstance(exc, MissingRequiredArgument):                           #If action command only bot, then TURN OFF
			await ctx.send("One or more required arguments are missing.")
		elif isinstance(exc, MissingPermissions):
			await ctx.send("You do not have the required permissions to execute that command. (If you do, check the channel permissions.)")	
		elif isinstance(exc, BotMissingPermissions):
			await ctx.send("I do not have the required permissions to execute that task.")

		elif hasattr(exc, "original"):
			# if isinstance(exc.original, HTTPException):
			# 	await ctx.send("Unable to send message.")

			if isinstance(exc.original, Forbidden):                          #TURN THIS ON
				await ctx.send("I do not have permission to do that.")

			else:
				raise exc.original

		else:
			raise exc



	async def on_ready(self):
		if not self.ready:
			self.guild = self.get_guild(774009780913045524)
			self.stdout = self.get_channel(804978388212252672)
			self.scheduler.start()
			self.update_db()

			meta = self.get_cog("Meta")
			await meta.set()


			while not self.cogs_ready.all_ready():
				await sleep(0.5)

			await self.stdout.send(f"Missed you {self.owner} <333. Ready when you are!")
			self.ready = True
			print("Sayuri is UP and RUNNING.")

		else:
			print("Sayuri reconnected.")

	@Cog.listener()
	async def on_message(self, message):
		if not message.author.bot:
			if isinstance(message.channel, DMChannel):
				if len(message.content) < 50:
					await message.channel.send("Your message should be at least 50 characters in length.")

				else:
					member = self.guild.get_member(message.author.id)
					embed = Embed(title="Modmail Received!",
								  colour=(0xa451d8),
								  timestamp=datetime.utcnow())

					embed.set_thumbnail(url=member.avatar_url)

					fields = [("Member", member.mention, False),
							  ("Message", message.content, False)]

					for name, value, inline in fields:
						embed.add_field(name=name, value=value, inline=inline)
					
					mod = self.get_cog("Mod")
					await mod.modmail.send(embed=embed)
					await message.channel.send("Alrighty! Your message has been relayed to the moderators. Thanks for reporting the situation ^^")

			else:
				await self.process_commands(message)


bot = Bot()




