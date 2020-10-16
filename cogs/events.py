import discord
from bot import *
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game("mogu mogu!"))
        print("{} has logged in.".format(self.client.user))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.client.get_channel(channel_id).send(
            f"Hey {member.mention} Welcome to **{member.guild.name}**!"
        )

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.client.get_channel(channel_id).send(
            f"{member.name}#{member.discriminator} just left the server."
        )


def setup(client):
    client.add_cog(Events(client))
