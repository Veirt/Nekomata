# Import necessary packages
import datetime
import os
import urllib.request
from os import getenv
from shutil import move

import discord
from discord.ext import commands, tasks

import database

now = datetime.datetime.now()
filename = ("PatchInfoServer.cfg",)
url = ("http://10.6.11.11/Patch/PatchInfoServer.cfg",)
