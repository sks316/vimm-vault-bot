import nextcord
from nextcord.ext import commands
import vimm_config as config

botver = "vimm-vault-bot v1.1"

async def get_dev(self):
    dev = self.bot.get_user(config.owner)

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f":ping_pong: Pong! **{self.bot.latency * 1000:.0f}**ms")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f":ping_pong: Ping! **{self.bot.latency * 1000:.0f}**ms")

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = nextcord.Embed(title=botver, description="The command prefix is `v.`. To run a command, you must begin a message with `v.`.", color=0x7289da)
        embed.add_field(name="The Vault:", value="**v.lookup** - Looks for a game in The Vault and returns the results. (Not yet implemented) Aliases: **v.search**\n**v.request** - Requests for a game to be added to The Vault. (Not yet implemented)", inline=False)
        embed.add_field(name="Bot:", value="**v.info** - See information about the bot, such as its uptime and a link to the source code.\n**v.ping** - Returns the bot's latency. Aliases: **v.pong**\n**v.bug** - Submit a bug report if anything goes wrong. This is not to be used for bugs in Vimm's Lair, only for bugs in this bot. \n**v.suggest** - Want to see something added to the bot? Suggest it! This is not to be used for suggestions for Vimm's Lair, only for suggestions for this bot.", inline=False)
        embed.set_footer(text=botver + " by PrincessLillie#2523", icon_url=self.bot.user.avatar.url)
        await ctx.message.author.send(embed=embed)
        await ctx.message.add_reaction("✅")

def setup(bot):
    bot.add_cog(General(bot))
