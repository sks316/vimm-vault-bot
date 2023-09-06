import disnake
from disnake.ext import commands
import os
import random

botstatus = [
    'Nintendo Entertainment System',
    'Super Nintendo Entertainment System',
    'Nintendo 64',
    'Nintendo GameCube',
    'Nintendo Wii',
    'Nintendo Wii U',
    'Nintendo Switch',
    'Game Boy',
    'Virtual Boy',
    'Game Boy Color',
    'Game Boy Pocket',
    'Game Boy Micro',
    'Game Boy Advance',
    'Nintendo DS',
    'Nintendo 3DS',
    'PlayStation',
    'PlayStation 2',
    'PlayStation 3',
    'PlayStation 4',
    'PlayStation 5',
    'PlayStation Portable',
    'PlayStation Vita',
    'PlayStation TV',
    'SEGA Master System',
    'SEGA Genesis',
    'SEGA Saturn',
    'SEGA Dreamcast',
    'SEGA Game Gear',
    'SEGA Pico',
    'SEGA 32X',
    'XBOX',
    'XBOX 360',
    'XBOX One',
    'XBOX Series X',
    'Atari 2600',
    'Atari 5200',
    'Atari 7800',
    'Atari Jaguar',
    'Atari Lynx',
    'Atari VCS',
    'with /faq',
    'with Vimm',
    'with Player1041',
    'on an emulator',
    'with No-Intro',
    'with Redump',
    'games from the vault',
    'around in #vault-updates',
    'around in The Vault',
    'with files',
    'a hidden game...',
    'with the classics, preserved since 1997!'
]


class badmin(commands.Cog):

    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot
    
    async def cog_slash_command_check(self, inter: disnake.CommandInteraction) -> bool:
        role = inter.guild.get_role(1115106512411570246)
        return role in inter.author.roles

    async def cog_slash_command_error(
        self, inter: disnake.CommandInteraction, error: Exception
    ) -> None:
        if isinstance(error, commands.CheckFailure):
            await inter.response.send_message(
                "You do not have the required role to use this command.", ephemeral=True
            )
            return

        raise
    
    @commands.slash_command()
    async def clearterm(self, inter):
        """Admin: Clears terminal."""
        os.system('clear')
        os.system('cls')
        await self.bot.on_ready()
        await inter.response.send_message("✅ Done! Check your console!")
    '''
    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')
    @commands.slash_command()
    async def eval(self, inter, *, body: str):
        msg = await inter.send("<a:loading:598027019447435285> Evaluating...")
        env = {
            'bot': self.bot,
            'inter': inter,
            'channel': inter.channel,
            'author': inter.author,
            'guild': inter.guild,
            'message': inter.message,
            '__': self._last_result
        }
        env.update(globals())
        body = self.cleanup_code(body)
        stdout = io.StringIO()
        to_compile = (f'async def func():\n{textwrap.indent(body, "  ")}')
        try:
            exec(to_compile, env)
        except Exception as e:
            return await msg.edit(content=f'```py\n{e.__class__.__name__}: {e}\n```')
        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await msg.edit(content=f':x: An error occurred while evaluating the code.\nTraceback is shown below.```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await msg.delete()
                await inter.message.add_reaction('\u2705')
            except Exception: 
                pass
    '''
    
    @commands.slash_command()
    async def changestatus(self, inter):
        """Admin: Randomizes bot status."""
        status = random.choice(botstatus)
        await self.bot.change_presence(activity=disnake.Game(name=status))
        await inter.response.send_message(f"The status was changed to `Playing {status}`.")
        
    @commands.slash_command()
    async def reloadcogs(self, inter):
        """Admin: Reload all loaded cogs."""
        await inter.response.defer()
        cogs = os.listdir('commands')
        for ext in cogs:
            if ext == '__pycache__':
                continue
            self.bot.reload_extension(f'commands.{ext[:-3]}')
        await inter.send("Cogs reloaded.")
    
    
def setup(bot):
    bot.add_cog(badmin(bot))
    print('| Bot Admin - Loaded')