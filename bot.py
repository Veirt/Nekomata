import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
# .env Configuration
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
token = os.getenv("TOKEN")
channel_id = int(os.getenv("CHANNEL"))
prefix = os.getenv("PREFIX")

# Prefix
client = commands.Bot(prefix, intents=intents)

# Load Cogs
startup_extension = ("cogs.commands", "cogs.events")
for ext in startup_extension:
    client.load_extension(ext)

client.run(token)
