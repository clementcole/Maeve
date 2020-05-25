import discord
from discord.ext import commands
import requests
import time
import asyncio

class Utility_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Utility_Commands(client))