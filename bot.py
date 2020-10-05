import discord
import datetime
import urllib.request
from command import *
from config import *
from discord.ext import commands, tasks
from shutil import move
from os import getenv

now = datetime.datetime.now()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("mogu mogu!"))
    print("{} has logged in.".format(client.user))


@tasks.loop(seconds = 5.0)
async def Check_Loop():
    message_channel = client.get_channel(channel_id)
    # Get vesion from URL
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
    message_channel = client.get_channel(channel_id)


Check_Loop.start()
client.run(token)