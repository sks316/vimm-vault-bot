import disnake
from disnake.ext import commands, tasks
import aiohttp
import os
import pytz
import json
from datetime import datetime

class vault(commands.Cog):
    
    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot
        self.vault_update.start()
    
    @tasks.loop(minutes=1.0)
    async def vault_update(self):
        vault = self.bot.get_channel(1000164073536753774)
        
        if os.path.exists("timestamp.txt"):
            with open('timestamp.txt', 'r') as file:
                timestamp = file.read()
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://vimm.net/api/uploads.php?since={timestamp}") as results:
                    results = await results.text()
                    try:
                        games = json.loads(results)
                        timezone = pytz.timezone("Etc/GMT")
                        timestamp = datetime.now(timezone)
                        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                        
                        with open('timestamp.txt', 'w') as file:
                            file.write(timestamp)
                            file.close()
                    except:
                        games = { "results": [] }
                        pass
                        
                    
            try:
                for x in games['results']:
                    game = x['title']
                    system = x['system']
                    url = x['url']
                    
                    
                    try:
                        await vault.send(f"`{system}: {game}` has been uploaded to The Vault. \n<{url}>")
                    except:
                        pass
                    
            except:
                pass
        
        else:
            timezone = pytz.timezone('Etc/GMT')
            timestamp = datetime.now(timezone)
            timestamp = timestamp.strftime("%Y-%m-%d %H%M%S")
            with open('timestamp.txt', 'w') as file:
                file.write(timestamp)
                file.close()

def setup(bot):
    bot.add_cog(vault(bot))
    print("| Vault - Loaded")