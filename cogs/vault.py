import discord
from discord.ext import tasks, commands
import asyncio
from datetime import datetime
import pytz
import json
import aiohttp
import os
import vimm_config as config

botver = "vimm-vault-bot v1.0"

class Vault(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vault_updates.start()
		  
    @commands.command(aliases=["search"])
    async def lookup(self, ctx):
        await ctx.send("This command has yet to be added, as the current implementation of the Vimm's Lair API does not support searching The Vault. Should an update to the API be made that supports searching, I will add this command as soon as possible.")
		  
    @commands.command()
    async def request(self, ctx):
        await ctx.send("This command is not yet implemented. I hope to implement this fully in the future, so please look forward to it.")

    @tasks.loop(minutes=1)
    async def vault_updates(self):
        #--first we get the channel to post updates to, this is specified in the config file that we imported earlier so we can call the channel ID with config.updates_channel--#
        channel = self.bot.get_channel(config.updates_channel)
        #--now we get the timestamp, if the timestamp file doesn't exist then we store the current timestamp as timestamp.txt and end--#
        if os.path.exists("timestamp.txt"):
            #--Next we read the timestamp from the file and store it as "timestamp"--#
            with open('timestamp.txt', 'r') as f:
                timestamp = f.read()
		      #--Now we get recently-uploaded games from the Vimm's Lair API using the stored timestamp in an fstring, using async and aiohttp instead of requests so as to not cause blocking--#
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://vimm.net/api/uploads.php?since={timestamp}') as result:
                    results = await result.text()
                    #--the API returns results in JSON format, so we parse it as JSON using the JSON module and store it as "games"--#
                    try:
                        games = json.loads(results)
                        #--the API uses GMT-01:00, which is equivalent to Azores Standard Time, or Atlantic/Azores. We use the third-party library pytz in conjunction with Python's built-in datetime module to get the timezone of Atlantic/Azores--#
                        timezone = pytz.timezone('Atlantic/Azores')
                        timestamp = datetime.now(timezone)
                        #--then we format it properly so we can interact with the API using this timestamp--#
                        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                        #--and then save it to timestamp.txt, overwriting any previously-saved timestamp--#
                        with open('timestamp.txt', 'w') as f:
                            f.write(timestamp)
                    #--if the JSON parsing fails, we handle the error accordingly--#
                    except:
                        games = { "results": [] }
                        pass
            #--now we take the JSON we loaded earlier, and get all the items in games[results]. If there are none, this does nothing and silently fails, negating the need for further error handling--#
            try:
                for x in games['results']:
                    #--we take the game title and the game system and store them accordingly--#
                    game = x['title']
                    system = x['system']
                    #--finally, we return this information to Discord in our specified channel--#
                    try:
                        await channel.send(f"`{system}: {game}` has been uploaded to The Vault.")
                    except:
                        pass
            except:
                pass
        #--if the timestamp.txt doesn't exist, then we make a new one--#
        else:
            #--the API uses GMT-01:00, which is equivalent to Azores Standard Time, or Atlantic/Azores. We use the third-party library pytz in conjunction with Python's built-in datetime module to get the timezone of Atlantic/Azores--#
            timezone = pytz.timezone('Atlantic/Azores')
            timestamp = datetime.now(timezone)
            #--next we format it properly so we can interact with the API using this timestamp--#
            timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            #--finally, we make a new file named timestamp.txt and save it there--#
            with open('timestamp.txt', 'w') as f:
                f.write(timestamp)
	 
def setup(bot):
    bot.add_cog(Vault(bot))
