
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
    async def who(self, ctx):
        await ctx.send("You are {}".format(ctx.message.author))

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
