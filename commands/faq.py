import disnake
from disnake.ext import commands

class help(commands.Cog):

    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot
        
    @commands.slash_command()
    async def faq(self, inter):
        return
    
    @faq.sub_command()
    async def help(self, inter):
        """A list of commands for the FAQs."""
        embed = disnake.Embed(
            title = "FAQ Help",
            description = "/faq altdl - Links to alternative download sites.\n/faq bios - Links to a list of BIOS files.\n/faq filetype - Shows what the file extension of each game is expected to be."
        )
        await inter.response.send_message(embed = embed)
    
    @faq.sub_command()
    async def altdl(self, inter):
        """Links to alternative download sites."""
        embed = disnake.Embed(
            title = "Alternative Downloads",
            description = "These sites are __trusted__ and are safe to use.\n**hShop** - https://hshop.erista.me - 3DS\n**Myrient** - https://myrient.erista.me - All of Vimm's plus more. Download Wii games from here if using Dolphin as they download to .rvz which is incompatible with the Wii console.\n**edge|emulation** - https://edgeemu.net/ - Pre Wii era and arcade games.\n**Ghostware Archive.org** - https://archive.org/search?query=Ghostware - Working ROMs for many consoles, in parted lists though. Add the name of the console to the end of the search for specific consoles. Download Wii games for consoles or Dolphin here as they download to .wbfs which works on both.\n**My Abandonware** - https://www.myabandonware.com/ - Old 'abandoned' games for PC."
        ).set_footer(text = "If you have any extra sites, ping @Player1041#3716 with the site link.", icon_url = self.bot.owner.avatar.url)
        await inter.response.send_message(embed = embed)

    @faq.sub_command()
    async def bios(self, inter):
        """Links to a list of BIOS files."""
        embed = disnake.Embed(
            title = "BIOS Files",
            description = "https://emulation.gametechwiki.com/index.php/Emulator_files"
        )
        await inter.response.send_message(embed = embed)

    @faq.sub_command()
    async def filetype(self, inter):
        """Shows what the file extension of each game is expected to be."""
        embed = disnake.Embed(
            title = "File Types",
            description = "**.7z / .zip / .rar** - These are compressed archives of files. You need software to open them. I personally recommend [7-Zip](https://7-zip.org)(https://7-zip.org) for this.\nFor any **.bin/.cue** files or JB folders, you need to keep them in a folder, they do not work by themselves.\n**NES** - .nes\n**Master System** - .sms\n**Genesis / Mega Drive** - .md\n**Game Boy** - .gb\n**SNES** - .snes\n**Saturn** - .bin/.cue\n**PlayStation** - .bin/.cue\n**Virtual Boy** - .vb\n**Nintendo 64** - .n64\n**Game Boy Colour** - .gbc\n**Dreamcast** - .bin/.cue or .gdi\n**PlayStation 2** - .iso\n**XBOX** - .xiso.iso (only on emulators) or .iso (don't work on emulators but work on consoles)\n**GameCube** - .nkit.iso (avoid using it for [reasons](https://www.reddit.com/r/DolphinEmulator/comments/lflp5m/is_nkit_really_as_bad_as_it_is_made_out_to_be/)) or .ciso (generally better than .nkit.iso because of [improved compatibility with Dolphin and console](https://vimm.net/bbs/?p=viewPost&Post=27668)) or .iso\n**Game Boy Advance** - .gba\n**Nintendo DS** - .nds\n**PlayStation Portable** - .iso\n**XBOX 360** - .iso\n**PlayStation 3** - JB Folder\n**Nintendo Wii** - .wbfs (best file format in my opinion) or .iso or .rvz (only on Dolphin) or .wad (installs to the Wii Channel, used mainly in WiiWare, best to avoid it if other formats work)\n**Nintendo 3DS** - .cia\n**Nintendo Wii U** - .wud or .wux\n**Playstation Vita** - .vpk or .pkg\n**Nintendo Switch** - .xci or .nsp\n**MAME / Arcade** - Keep all the files in a folder."
        )
        await inter.response.send_message(embed = embed)

def setup(bot):
    bot.add_cog(help(bot))
    print('| FAQ - Loaded')