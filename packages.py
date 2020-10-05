# Import necessary packages
import discord
import datetime
import urllib.request
import os
from config import *
from discord.ext import commands, tasks
from shutil import move
from os import getenv

now = datetime.datetime.now()