import discord
from discord.ext import commands
import os # needed for env
from dotenv import load_dotenv # env

load_dotenv("token.env")
token = os.getenv('token')


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Nooty Noot is locked and loaded.")

bot.load_extension("cogs.reddit")
bot.run(token)
