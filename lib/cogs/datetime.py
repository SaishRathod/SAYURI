from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from aiohttp import request
from discord.ext.commands import is_owner
from geopy import geocoders
from geopy.geocoders import Nominatim
from tzwhere import tzwhere

class Datetime(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("datetime")

	@command(name = "datetime", aliases = ["time","dt",], brief = "Find the date and time of the specified city.")
	@is_owner()
	async def datetime_command(self, ctx, *, location:str):
		await ctx.send("Searching... ")
		async with ctx.typing():
			g = geocoders.Nominatim(user_agent = "smrathod2004@gmail.com")
			location = g.geocode(f"{location}")
			tz = tzwhere.tzwhere()
			timezone = (tz.tzNameAt(location.latitude, location.longitude))

			datetime_url = f"https://timezoneapi.io/api/timezone/?timezone={timezone}&token=alozcHkAuzkZYfnogmxD"

			async with request("GET", datetime_url, headers = {}) as response:
				data = await response.json()
				if response.status == 200:
					Location = data['data']['timezone']['location']
					Time = data['data']['datetime']['date_time_txt']

					await ctx.send(f"Time in **{location}**: \n{Time}")

				else:
					await ctx.send(f"API sent a {response.status} response.")



def setup(bot):
	bot.add_cog(Datetime(bot))