import os
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name = GUILD)

    print(f'{client.user} has connected to Discord!')

@bot.command(name='play')
async def play_music(ctx, search_str):
    pass

    
    

bot.run(TOKEN)