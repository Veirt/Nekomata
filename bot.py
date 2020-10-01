import discord
import os
import datetime
import shutil
import urllib.request
from config import *
from hasher import sha1
from discord.ext import commands, tasks

""" prefix = os.getenv('PREFIX')
channel_id = os.getenv('CHANNEL')
token = os.getenv('TOKEN') """


client = commands.Bot(prefix)
now = datetime.datetime.now()
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("mogu mogu!"))
    print("{} has logged in.".format(client.user))

@tasks.loop(seconds = 5.0)
async def Check_Loop():
    message_channel = client.get_channel(channel_id)
    filename = 'PatchInfoServer.cfg'
    # download file
    url = 'http://10.6.11.11/Patch/PatchInfoServer.cfg'
    urllib.request.urlretrieve(url, filename)

    # get hashes
    hash_latest =sha1('latest/PatchInfoServer.cfg')
    hash_new = sha1(filename)

    # compare hashes
    if hash_latest != hash_new:
        print("There is an update")
        f = open("latest/PatchInfoServer.cfg", "r")
        f2 = open("PatchInfoServer.cfg", "r")
        latestVer = f.read()
        newVer = f2.read()
        embed = discord.Embed(title = "Update Notice", description = "Mogu mogu! Miku DN has patched from {} to {} ".format(latestVer, newVer), colour = discord.Colour.blue())
        embed.set_footer(text="{}-{}-{}".format(now.year,now.month,now.day))
        await message_channel.send(embed=embed)
        f.close()
        f2.close()
        shutil.move('PatchInfoServer.cfg', 'latest/PatchInfoServer.cfg')
    else:
        pass


@Check_Loop.before_loop
async def before():
    await client.wait_until_ready()
    message_channel = client.get_channel(channel_id)

@client.command()
async def mogu(ctx):
    await ctx.send("okayu!")

@client.command()
async def check(ctx):
    f = open("latest/PatchInfoServer.cfg", "r")
    await ctx.send(f.read())
    f.close()

Check_Loop.start()
client.run(token)