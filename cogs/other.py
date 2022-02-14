import nextcord
from nextcord.ext import commands
import vimm_config as config

botver = "vimm-vault-bot v1.1"

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def bug(self, ctx, *, arg):
        dev = self.bot.get_user(config.owner)
        embed = nextcord.Embed(title="⚠ Bug Report", description=arg, color=0xff0000)
        embed.set_footer(text="Submitted by " + ctx.author.name + "#" + ctx.author.discriminator + " - " + botver + " by PrincessLillie#2523", icon_url=ctx.author.avatar.url)
        await dev.send(embed=embed)
        await ctx.send("✅ Successfully sent in your bug report! Thank you for helping to make this bot better. \nIf you want to provide further details, send a DM to **" + dev.name + "#" + dev.discriminator + "**.")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def suggest(self, ctx, *, arg):
        dev = self.bot.get_user(config.owner)
        embed = nextcord.Embed(title="💭 Suggestion", description=arg, color=0x7289da)
        embed.set_footer(text="Submitted by " + ctx.author.name + "#" + ctx.author.discriminator + " - " + botver + " by PrincessLillie#2523", icon_url=ctx.author.avatar.url)
        await dev.send(embed=embed)
        await ctx.send("✅ Successfully sent in your suggestion! Thank you for helping to make this bot better. \nIf you want to provide further details, send a DM to **" + dev.name + "#" + dev.discriminator + "**.")

def setup(bot):
    bot.add_cog(Other(bot))
