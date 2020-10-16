# Import packages
import discord
from discord.ext import commands, tasks
import os

intents = discord.Intents.default()
intents.members = True
# Virtual Environment
token = os.getenv('TOKEN')
channel_id = int(os.getenv('CHANNEL'))
prefix = os.getenv('PREFIX')

# Prefix
client = commands.Bot(prefix, intents=intents)

# Load Cogs
startup_extension = ("cogs.commands", "cogs.events", "cogs.tasks")
for ext in startup_extension:
    client.load_extension(ext)

client.run(token)
