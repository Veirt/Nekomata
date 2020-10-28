import re
import datetime
import urllib.request
from shutil import move

from bot import *
from discord.ext import commands, tasks
from lib import *


class CheckVer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Check_Loop.start()

    @tasks.loop(seconds=30.0)
    async def Check_Loop(self):
        def get_time():
            return datetime.date.today(), datetime.datetime.now().time()

        message_channel = self.client.get_channel(channel_id)
        for i in urls_and_files.values():
            url, file_name, server = i

            # Get Time Now
            date, time = get_time()
            print(f"{date} {time} Checking {server}")

            # Defining newVer
            with urllib.request.urlopen(url) as cfg:
                newVer = re.search(b"^[vV]ersion\s[0-9]*", cfg.read()).group(0).decode("utf-8")

            # Defining latestVer
            with open(f"latest/{file_name}", "r") as f:
                latestVer = re.search("^[vV]ersion\s[0-9]*", f.read()).group(0)

            if newVer != latestVer:
                urllib.request.urlretrieve(url, file_name)
                print("There is an update")
                embed = discord.Embed(
                    title="Update Notice",
                    description=f"Mogu mogu! {server} patched from {latestVer[8:]} to {newVer[8:]} ",
                    colour=discord.Colour(0xE5D1ED),
                )

                embed.set_footer(text=date)
                await message_channel.send(embed=embed)
                move(f"{file_name}", f"latest/{file_name}")

    @Check_Loop.before_loop
    async def before(self):
        await self.client.wait_until_ready()


def setup(client):
    client.add_cog(CheckVer(client))
