import datetime
# import logging
import urllib.request
from shutil import move

from bot import *
from discord.ext import commands, tasks
from lib import *

# Log Configuration
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')


class CheckVer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Check_Loop.start()

    @tasks.loop(seconds=30.0)
    # Testing : seconds=15.0
    # Run : hours=1.0
    async def Check_Loop(self):
        def get_time():
            """
            Get date and time now
            :return: date and time now
            """
            return datetime.date.today(), datetime.datetime.now().time()

        message_channel = self.client.get_channel(channel_id)
        remove_nl = lambda text: text.replace("\n", "")
        for i in urls_and_files.values():
            url, file_name, server = i
            # logging.debug(f"Checking {server}")
            # Get Time Now
            date, time = get_time()
            print(f"{date} {time} Checking {server}")
            cfg = urllib.request.urlopen(url)

            # Use different way to US since US has unique version.cfg
            if server == "US":
                urllib.request.urlretrieve(url, file_name)
                with open(file_name) as f:
                    newVer = f.readline()
                    newVer = remove_nl(newVer)

                with open(f"latest/{file_name}") as f:
                    latestVer = f.readline()
                    latestVer = remove_nl(latestVer)

                if newVer != latestVer:
                    print("There is an update")
                    embed = discord.Embed(
                        title="Update Notice",
                        description=f"Mogu mogu! {server} patched from {latestVer[8:]} to {newVer[8:]} ",
                        colour=discord.Colour(0xE5D1ED),
                    )

                    embed.set_footer(text=date)
                    await message_channel.send(embed=embed)
                    move(f"{file_name}", f"latest/{file_name}")
                else:
                    os.remove(file_name)

            else:
                newVer = ""
                for x in cfg:
                    newVer = x.decode("utf-8").split()
                    newVer = " ".join(newVer)
                # Defining latestVer
                with open(f"latest/{file_name}", "r") as f:
                    latestVer = f.readline()
                    latestVer = "".join(latestVer)
                    latestVer = remove_nl(latestVer)

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
