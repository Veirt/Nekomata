import discord
import os
import shutil
import urllib.request
from config import *
from hasher import sha1
from discord.ext import commands, tasks

client = commands.Bot(command_prefix= '.')

print("Bot is ready!")

@tasks.loop(seconds = 5.0)
async def Check_Loop():
    message_channel = client.get_channel(target_channel_id)
    filename = 'PatchInfoServer.cfg'
    # download file
    url = 'http://10.6.11.11/Patch/PatchInfoServer.cfg'
    urllib.request.urlretrieve(url, filename)

    # get hashes
    hash_latest = sha1('latest/PatchInfoServer.cfg')
    hash_new = sha1(filename)

    # compare hashes
    if hash_latest != hash_new:
        print("There is an update")
        f = open("latest/PatchInfoServer.cfg", "r")
        f2 = open("PatchInfoServer.cfg", "r")
        latestVer = f.read()
        newVer = f2.read()
        await message_channel.send("Mogu mogu! {} to {}".format(latestVer, newVer))
        f.close()
        f2.close()
        shutil.move('PatchInfoServer.cfg', 'latest/PatchInfoServer.cfg')
    else:
        pass


@Check_Loop.before_loop
async def before():
    await client.wait_until_ready()
    message_channel = client.get_channel(target_channel_id)



Check_Loop.start()
client.run(token)