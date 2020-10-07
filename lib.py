# Import necessary packages
import discord
import datetime
import urllib.request
import os
import database
from discord.ext import commands, tasks
from shutil import move
from os import getenv


now = datetime.datetime.now()
filename = ("PatchInfoServer.cfg",)
url = ("http://10.6.11.11/Patch/PatchInfoServer.cfg",)
