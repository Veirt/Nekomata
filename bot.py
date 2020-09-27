import discord
import os
import shutil
import urllib.request
from config import token
from hasher import sha1
from discord.ext import commands

client = commands.Bot(command_prefix= '.')

print("Bot is ready!")

@client.command()
async def check(ctx):
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
        await ctx.send("{} to {}".format(latestVer, newVer))
        f.close()
        f2.close()
        shutil.move('PatchInfoServer.cfg', 'latest/PatchInfoServer.cfg')
    else:
        print("There is no update")
        pass
    

client.run(token)