# Import packages
from packages import *

# Virtual Environment
token = getenv('TOKEN')
channel_id = int(getenv('CHANNEL'))

# Prefix
client = commands.Bot("mogu ")


""" # Load cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}") """


for ext in os.listdir("cogs/"):
    if ext.endswith(".py"):
        client.load_extension(f"cogs.{ext[:-3]}")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("mogu mogu!"))
    print("{} has logged in.".format(client.user))


@tasks.loop(seconds = 5.0)
async def Check_Loop():
    message_channel = client.get_channel(channel_id)
    # Get version from URL
    file = urllib.request.urlopen(url[0])
    for x in file:
        newVer = x.decode("utf-8")

    f = open("latest/PatchInfoServer.cfg", "r")
    latestVer = f.read()

    if newVer != latestVer:
        urllib.request.urlretrieve(url[0], filename[0])
        print("There is an update")
        embed = discord.Embed(title = "Update Notice", description = "Mogu mogu! Patched from {} to {} ".format(latestVer[-3:], newVer[-3:]), colour = discord.Colour(0xe5d1ed))
        embed.set_footer(text="{}-{}-{}".format(now.year,now.month,now.day))
        await message_channel.send(embed=embed)
        f.close()
        move('PatchInfoServer.cfg', 'latest/PatchInfoServer.cfg')

    file.close()


@Check_Loop.before_loop
async def before():
    await client.wait_until_ready()


Check_Loop.start()
client.run(token)