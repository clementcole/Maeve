import discord
from discord.ext import commands
import requests
import time
import asyncio


class ServerStats(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(ServerStats(client))