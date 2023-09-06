import disnake
from disnake.ext import commands
import aiohttp
import json
from dotenv import load_dotenv
import os
import random

load_dotenv()
catapi = os.environ['catkey']
dogapi = os.environ['dogkey']
animalList = ['Random', 'Cats', 'Dogs', 'Ducks', 'Foxes', 'Pandas', 'Red Pandas', 'Koalas', 'Birds', 'Bunnies', 'Whales', 'Kangaroos', 'Raccoons', 'Pikachu?']

class animals(commands.Cog):
    
    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot

    @commands.slash_command()
    async def animals(self, inter):
        """Displays an animal photo."""
        await inter.response.send_message("Select an animal.", components = disnake.ui.StringSelect(options = animalList))
        
    @commands.Cog.listener("on_dropdown")
    async def animalDropdown(self, inter: disnake.MessageInteraction):
        selected = inter.values[0]
        if selected == 'Random':
            selected = random.choice(animalList[1:])

        if selected == "Cats":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.thecatapi.com/v1/images/search?has_breeds=1&api_key={catapi}") as resp:
                    data = json.loads(await resp.text())
                    catEmbed = disnake.Embed(
                        title = "Cats!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data[0]['url']
                    ).set_footer(
                        text = f"This is a {data[0]['breeds'][0]['name']} cat.")
            await inter.response.send_message(embed = catEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Dogs":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.thedogapi.com/v1/images/search?has_breeds=1&api_key={dogapi}") as resp:
                    data = json.loads(await resp.text())
                    dogEmbed = disnake.Embed(
                        title = "Dogs!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data[0]['url']
                    ).set_footer(
                        text = f"This is a {data[0]['breeds'][0]['name']} dog.")
            await inter.response.send_message(embed = dogEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Ducks":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://random-d.uk/api/v2/quack") as resp:
                    data = json.loads(await resp.text())
                    duckEmbed = disnake.Embed(
                        title = "Ducks!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['url']
                    ).set_footer(
                        text = data['message'])
            await inter.response.send_message(embed = duckEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Foxes":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://some-random-api.com/animal/fox") as resp:
                    data = json.loads(await resp.text())
                    foxEmbed = disnake.Embed(
                        title = "Foxes!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['image']
                    ).set_footer(
                        text = data['fact'])
            await inter.response.send_message(embed = foxEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Pandas":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://some-random-api.com/animal/panda") as resp:
                    data = json.loads(await resp.text())
                    pandaEmbed = disnake.Embed(
                        title = "Pandas!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['image']
                    ).set_footer(
                        text = data['fact'])
            await inter.response.send_message(embed = pandaEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Red Pandas":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://some-random-api.com/animal/red_panda") as resp:
                    data = json.loads(await resp.text())
                    redPandaEmbed = disnake.Embed(
                        title = "Red Pandas!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['image']
                    ).set_footer(
                        text = data['fact'])
            await inter.response.send_message(embed = redPandaEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Koalas":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://some-random-api.com/animal/koala") as resp:
                    data = json.loads(await resp.text())
                    koalaEmbed = disnake.Embed(
                        title = "Koalas!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['image']
                    ).set_footer(
                        text = data['fact'])
            await inter.response.send_message(embed = koalaEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Birds":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://some-random-api.com/animal/bird") as resp:
                    data = json.loads(await resp.text())
                    birdEmbed = disnake.Embed(
                        title = "Birds!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['image']
                    ).set_footer(
                        text = data['fact'])
            await inter.response.send_message(embed = birdEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Bunnies":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.bunnies.io/v2/loop/random/?media=gif,png") as resp:
                    data = json.loads(await resp.text())
                    bunnyEmbed = disnake.Embed(
                        title = "Bunnies!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['media']['gif']
                    ).set_footer(
                        text = "Powered by bunnies.io")
            await inter.response.send_message(embed = bunnyEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Whales":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://some-random-api.com/img/whale") as resp:
                    data = json.loads(await resp.text())
                    whaleEmbed = disnake.Embed(
                        title = "Whales!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['link']
                    ).set_footer(
                        text = "Powered by some-random-api.com")
            await inter.response.send_message(embed = whaleEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Kangaroos":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://some-random-api.com/animal/kangaroo") as resp:
                    data = json.loads(await resp.text())
                    kangarooEmbed = disnake.Embed(
                        title = "Kangaroo!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['image']
                    ).set_footer(
                        text = data['fact'])
            await inter.response.send_message(embed = kangarooEmbed, components = disnake.ui.StringSelect(options = animalList))

        elif selected == "Raccoons":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://some-random-api.com/animal/raccoon") as resp:
                    data = json.loads(await resp.text())
                    raccoonEmbed = disnake.Embed(
                        title = "Raccoons!",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['image']
                    ).set_footer(
                        text = data['fact'])
            await inter.response.send_message(embed = raccoonEmbed, components = disnake.ui.StringSelect(options = animalList))
        
        elif selected == "Pikachu?":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://some-random-api.com/img/pikachu") as resp:
                    data = json.loads(await resp.text())
                    pikaEmbed = disnake.Embed(
                        title = "Pikachu!?",
                        colour = disnake.Colour.random()
                    ).set_image(
                        url = data['link']
                    ).set_footer(
                        text = "Powered by some-random-api.com")
            await inter.response.send_message(embed = pikaEmbed, components = disnake.ui.StringSelect(options = animalList))

def setup(bot):
    bot.add_cog(animals(bot))
    print("| Animals - Loaded")