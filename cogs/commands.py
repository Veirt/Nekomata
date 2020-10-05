import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def mogu(self, ctx):
        await ctx.send("okayu!")


    @commands.command()
    async def check(self, ctx):
        f = open("latest/PatchInfoServer.cfg", "r")
        await ctx.send(f.read())
        f.close()


def setup(client):
    client.add_cog(Commands(client))