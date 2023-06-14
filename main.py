import time
import disnake
from disnake.ext import commands, tasks
from dotenv import load_dotenv
import platform
import os
import random

load_dotenv()
token = os.environ['token']
bot = commands.InteractionBot(
    intents = disnake.Intents.all(),
    test_guilds = [1000163838374727800, # - Player's Projects 
                844285548213567529 # - Vimm's Lair
                ],
    reload = True
)

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

print(f"\x1B[1;4mThe Vault\x1B[0m \n")
print("By Player1041")
print(f"\n\x1B[1;4mCommands\x1B[0m \n")
bot.load_extensions("commands")

@bot.event
async def on_ready():
    print(f"\n\x1B[1;4mStats\x1B[0m \n")
    print(f"| Name: {bot.user}")
    print(f"| ID: {bot.user.id}")
    print(f"| Latency: {round(bot.latency * 1000)}ms")
    print(f"| Server Count: {len(bot.guilds)}")
    print(f"| Total Users: {len(bot.users)}")
    print(f"| Disnake Version: {disnake.__version__}")
    print(f"| Python Version: {platform.python_version()}")
    await bot.change_presence(activity=disnake.Game(name=random.choice(botstatus)))

@tasks.loop(minutes=5.0)
async def change_status():
    await bot.change_presence(activity=disnake.Game(name=random.choice(botstatus)))

bot.run(token)

