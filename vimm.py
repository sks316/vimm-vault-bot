import nextcord
from nextcord.ext import tasks, commands
import asyncio
import random
import traceback
import sys
import datetime
import vimm_config as config

print('Starting... This may take some time.')
print('')

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='v.', intents=intents, owner_id=config.owner, case_insensitive=True)
cogs = ['cogs.general', 'cogs.other', 'cogs.admin', 'cogs.vault']

start_time = datetime.datetime.utcnow()

botver = "vimm-vault-bot v1.0"

#--List of playing statuses the bot can cycle through.--#
botstatus =[
   'with v.help',
   'with v.lookup',
   'games from The Vault',
	'in #vault-updates',
   'Preserving the Classics since 1997!',
	'with Redump',
	'with No-Intro',
	'with file hashes',
	'on an emulator',
	'Nintendo Entertainment System',
	'SEGA Genesis',
	'Super Nintendo Entertainment System',
	'SEGA Saturn',
	'PlayStation',
	'Nintendo 64',
	'SEGA Dreamcast',
	'PlayStation 2',
	'Xbox',
	'Nintendo GameCube',
	'PlayStation 3',
	'Wii',
	'WiiWare',
	'Game Boy',
	'Game Boy Color',
	'Game Boy Advance',
	'Nintendo DS',
	'PlayStation Portable',
]
        
@bot.event
async def on_ready():
    dev = bot.get_user(config.owner)
    print("The Vault Discord Bot, designed for Vimm's Lair")
    print('v1.0 by ' + dev.name + "#" + dev.discriminator + ' - Support: Not supported, see README.md')
    print('Logged into: ' + bot.user.name + "#" + bot.user.discriminator)
    print('------')

@tasks.loop(minutes=10.0)
async def change_status():
    playing = random.choice(botstatus)
    await bot.change_presence(activity=nextcord.Game(name=playing))

@change_status.before_loop
async def before_change_status():
    await bot.wait_until_ready()

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send(":wave: Done! See ya!")
    await bot.close()

@bot.command()
@commands.is_owner()
async def reload(ctx):
    for c in cogs:
        bot.unload_extension(c)
        bot.load_extension(c)
    await ctx.send(":white_check_mark: Successfully reloaded all cogs!")

@bot.command()
async def info(ctx):
    dev = bot.get_user(config.owner)
    now = datetime.datetime.utcnow() # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    embed = nextcord.Embed(title=botver, description="I'm a bot made to post new releases in The Vault at Vimm's Lair to a channel in the Vimm's Lair Discord server. In the future, I'll also be able to look up games in The Vault and request games to be uploaded to The Vault.", color=0x7289da)
    embed.add_field(name="Made by:", value=dev.name + "#" + dev.discriminator)
    embed.add_field(name="Uptime:", value="This bot has been online for {}".format(uptime_stamp), inline=False)
    embed.add_field(name="Source Code:", value="[My source code is available on GitHub.](https://github.com/sks316/vimm-vault-bot)", inline=False)
    embed.set_footer(text=botver + " by PrincessLillie#2523", icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.event
async def on_command_error(ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        
        ignored = (commands.CommandNotFound)
        error = getattr(error, 'original', error)
        
        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            err = await ctx.send(f':x: Sorry, **{ctx.command}** has been disabled.')
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, commands.UserInputError):
            err = await ctx.send(f':x: Please provide a valid argument and try again. For example, **p-{ctx.command} Super Mario World**.')
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, commands.NotOwner):
            err = await ctx.send(f':x: Sorry, you are not permitted to use the command **{ctx.command}**.')
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, commands.CommandOnCooldown):
            err = await ctx.send(":x: Sorry, you're being ratelimited for this command. Try again in **{:.2f}".format(error.retry_after) + "** seconds.")
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, nextcord.Forbidden):
            err = await ctx.send(f":x: I don't have sufficient permissions to do something. If you tried running **p-help**, make sure your DMs are open. Otherwise, please have an administrator check my permissions.")
            await ctx.message.delete(delay=10)
            return await err.delete(delay=10)

        elif isinstance(error, commands.NSFWChannelRequired):
            err = await ctx.send(f":x: You'll, uh, have to run that one in an NSFW channel.")
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                err = await ctx.author.send(f':x: Sorry, **{ctx.command}** can not be used in Private Messages.')
                await ctx.message.delete(delay=5)
                return await err.delete(delay=5)
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                err = await ctx.send(':x: I could not find that member. Please try again.')
                await ctx.message.delete(delay=5)
                return await err.delete(delay=5)
            
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        err = await ctx.send(':x: Sorry, an unknown error occurred. Please send a bug report with **p-bug**. Be sure to provide as many details as possible.')
        await ctx.message.delete(delay=10)
        await err.delete(delay=10)

change_status.start()
#--moved from on_ready, didn't know it was bad to load cogs in on_ready--#
for c in cogs:
    bot.load_extension(c)
bot.run(config.token)
