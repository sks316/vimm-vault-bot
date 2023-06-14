import disnake
from disnake.ext import commands

class admin(commands.Cog):

    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot

    '''@commands.slash_command
    async def kick(self, inter, user: disnake.Member, reason: str = ": No reason given."):
        await inter.guild.kick(member, reason)'''
def setup(bot):
    bot.add_cog(admin(bot))
    print('| Admin - Loaded')