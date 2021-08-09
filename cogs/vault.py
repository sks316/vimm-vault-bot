import discord
from discord.ext import commands
import asyncio
import datetime
import vimm_config as config

botver = "vimm-vault-bot v1.0"

class Vault(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
		  
    @commands.command(aliases=["search"])
    async def lookup(self, ctx):
        await ctx.send("This command has yet to be added, as the Vimm's Lair API is not yet ready. Work on this command will begin as soon as the API is ready, so please look forward to it.")
		  
    @commands.command()
    async def request(self, ctx):
        await ctx.send("This command has yet to be added, as the Vimm's Lair API is not yet ready. Work on this command will begin as soon as the API is ready, so please look forward to it.")

def setup(bot):
    bot.add_cog(Vault(bot))