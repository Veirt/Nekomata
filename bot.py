import discord
import os
import datetime
import shutil
import urllib.request
from discord.ext import commands, tasks

#Virtual Environment
token = os.getenv('TOKEN')
channel_id = int(os.getenv('CHANNEL'))


client = commands.Bot("mogu ")
now = datetime.datetime.now()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("mogu mogu!"))
    print("{} has logged in.".format(client.user))


@tasks.loop(seconds = 5.0)
async def Check_Loop():
    message_channel = client.get_channel(channel_id)
    filename = 'PatchInfoServer.cfg'
    # Get vesion from URL
    url = 'http://10.6.11.11/Patch/PatchInfoServer.cfg'
    file = urllib.request.urlopen(url)
    for line in file:
        version_now = line.decode("utf-8")
    
    f = open("latest/PatchInfoServer.cfg", "r")
    latestVer = f.read()
    if version_now != latestVer:
        urllib.request.urlretrieve(url, filename)
        print("There is an update")
        f2 = open("PatchInfoServer.cfg", "r")
        newVer = f2.read()
        embed = discord.Embed(title = "Update Notice", description = "Mogu mogu! Patched from {} to {} ".format(latestVer[-3:], newVer[-3:]), colour = discord.Colour(0xe5d1ed))
        embed.set_footer(text="{}-{}-{}".format(now.year,now.month,now.day))
        await message_channel.send(embed=embed)
        f.close()
        f2.close()
        shutil.move('PatchInfoServer.cfg', 'latest/PatchInfoServer.cfg')


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