from lib import *
from bot import *
import discord
from discord.ext import tasks


class CheckVer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Check_Loop.start()


    @tasks.loop(seconds=5.0)
    async def Check_Loop(self):
        global newVer
        message_channel = self.client.get_channel(channel_id)
        # Get version from URL
        file = urllib.request.urlopen(url[0])
        for x in file:
            newVer = x.decode("utf-8")

        f = open("latest/PatchInfoServer.cfg", "r")
        latestVer = f.read()

        if newVer != latestVer:
            database.query(newVer)
            urllib.request.urlretrieve(url[0], filename[0])
            print("There is an update")
            embed = discord.Embed(title="Update Notice",
                                  description=f"Mogu mogu! Patched from {latestVer[-3:]} to {newVer[-3:]} ",
                                  colour=discord.Colour(0xe5d1ed))

            embed.set_footer(text="{}-{}-{}".format(now.year, now.month, now.day))
            await message_channel.send(embed=embed)
            f.close()
            move('PatchInfoServer.cfg', 'latest/PatchInfoServer.cfg')

        file.close()

    @Check_Loop.before_loop
    async def before(self):
        await self.client.wait_until_ready()


def setup(client):
    client.add_cog(CheckVer(client))
