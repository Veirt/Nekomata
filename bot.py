# Import packages
from lib import *
intents = discord.Intents.default()
intents.members = True
# Virtual Environment
token = getenv('TOKEN')
channel_id = int(getenv('CHANNEL'))
prefix = getenv('PREFIX')

# Prefix
client = commands.Bot(prefix, intents=intents)

# Load Cogs
startup_extension = ("cogs.commands", "cogs.events", "cogs.tasks")
for ext in startup_extension:
    client.load_extension(ext)

client.run(token)
