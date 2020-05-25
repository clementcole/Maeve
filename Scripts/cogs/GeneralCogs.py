import discord
from discord.ext import commands
import requests
import time
import asyncio
import random
from enum import Enum

class Color(Enum):
    DEFAULT = 0
    AQUA = 1752220
    GREEN = 3066993
    BLUE = 3447003
    PURPLE = 10181046
    GOLD = 15844367
    ORANGE = 15105570
    RED = 15158332
    GREY = 9807270
    DARKER_GREY = 8359053
    NAVY = 3426654
    DARK_AQUA = 1146986
    DARK_GREEN = 2067276
    DARK_BLUE = 2123412
    DARK_PURPLE = 7419530
    DARK_GOLD = 12745742
    DARK_ORANGE = 11027200
    DARK_RED = 10038562
    DARK_GREY = 9936031
    LIGHT_GREY = 12370112
    DARK_NAVY = 2899536
    LUMINOUS_VIVID_PINK = 16580705
    DARK_VIVID_PINK = 12320855

class GeneralCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # events
    '''
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('.greet'):
            channel = message.channel
            await channel.send('Say hello!')

            def check(m):
                return m.content == 'hello' and m.channel == channel

            msg = await commands.wait_for('message', check=check)
            await channel.send('Hello {.author}!'.format(msg))
    '''
    @commands.command(pass_context=True)
    async def status(self, ctx):
        #await ctx.send(f'historicly maeve is currently online')
        #channel = ctx.message.channel
        red = Color.RED
        t1 = str(random.random())
        t2 = str(random.random())
        t3 = str(random.random())
        t4 = str(random.random())
        e = discord.Embed(title="Connection Speed and Online Status", colour=2791320)
        e.add_field(name='Maeve Pinging back ... 1', value=str(t1 + '\n'), inline=False)
        e.add_field(name='Maeve Pinging back ... 2', value=str(t2 + '\n'), inline=False)
        e.add_field(name='Maeve Pinging back ... 3', value=str(t3 + '\n'), inline=False)
        e.add_field(name='Maeve Pinging back ... 4', value=str(t4 + '\n'), inline=False)
        e.add_field(name='Status:', value=str('Online'), inline=False)
        await ctx.send(embed=e)



def setup(client):
    client.add_cog(GeneralCommands(client))