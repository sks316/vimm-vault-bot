import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os
import asyncpg
import asyncio

load_dotenv()
dbURL = os.environ['db_url']

class topten(commands.Cog):

    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot
        
    @commands.slash_command()
    async def topten(self, inter):
        return
    
    @topten.sub_command()
    async def config(self, inter):
        
        await inter.response.send_message("Under Development - Player1041")
    
    @topten.sub_command()
    async def view(self, inter):
        await inter.response.send_message("Under Development - Player1041")

def setup(bot):
    bot.add_cog(topten(bot))
    print('| Top Ten - Loaded')