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

    @commands.command()
    async def manualp(self, ctx, version):
        available = False
        if len(version) == 1:
            available = True
            version = f"00{version}"
        elif len(version) == 2:
            available = True
            version = f"0{version}"
        elif len(version) == 3:
            available = True
            version = f"{version}"
        if available:
            embed = discord.Embed(
                title=f"Manual Patch {version}",
                description=f"http://127.0.0.1/Patch/00000{version}/Patch00000{version}.pak",
                colour=discord.Colour(0xE5D1ED),
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send("The version is not available.")

    @manualp.error
    async def manual(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the manual patch version.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do the command!")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify an amount of messages to delete.")


def setup(client):
    client.add_cog(Commands(client))
