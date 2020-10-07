# Import packages
from packages import *

# Virtual Environment
token = getenv('TOKEN')
channel_id = int(getenv('CHANNEL'))
prefix = getenv('PREFIX')

# Prefix
client = commands.Bot(prefix)

# Load Cogs
startup_extension = ("cogs.commands", "cogs.events")
for ext in startup_extension:
    client.load_extension(ext)


@tasks.loop(seconds=5.0)
async def Check_Loop():
    global newVer
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
        embed = discord.Embed(title="Update Notice", description=f"Mogu mogu! Patched from {latestVer[-3:]} to {newVer[-3:]} ",colour=discord.Colour(0xe5d1ed))

        embed.set_footer(text="{}-{}-{}".format(now.year, now.month, now.day))
        await message_channel.send(embed=embed)
        f.close()
        move('PatchInfoServer.cfg', 'latest/PatchInfoServer.cfg')

    file.close()


@Check_Loop.before_loop
async def before():
    await client.wait_until_ready()


Check_Loop.start()
client.run(token)
