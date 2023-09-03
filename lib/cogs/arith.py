from discord.ext.commands import Cog, command, has_permissions, CheckFailure
from discord import Embed
from apscheduler.triggers.cron import CronTrigger
from discord import Activity, ActivityType
from discord.ext.commands import is_owner
from time import time
from datetime import datetime, timedelta
from typing import Optional

from ..db import db

class Arith(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("arith")


	@command(name = "calculate", aliases = ["arith", "cal", "calc"])
	@is_owner()
	async def calculate_command(self, ctx, operation, num1: int, num2: int):
		operations = ["add", "subtract", "multiply", "divide"]

		if operation == "add":

			result = num1 + num2 

			await ctx.send(f"The answer is: {result}") 

		elif operation == "subtract":

			result = num1 - num2 

			await ctx.send(f"The answer is: {result}") 

		elif operation == "multiply":

			result = num1 * num2

			await ctx.send(f"The answer is: {result}") 

		elif operation == "divide":

			try:
				result = num1 / num2 

				await ctx.send(f"The answer is: {result}") 

			except ZeroDivisionError:
				await ctx.send(f"Division by zero is undefined.")

		else:
			await ctx.send("Please specify a valid operation - (add, subtract, multiply, divide).")

def setup(bot):
	bot.add_cog(Arith(bot))