import discord
from discord.ext import commands
from discord.utils import get
import requests
import time
import asyncio
from stringcolor import *
import random


import datetime
probationary = 'probationary'
verified = 'everyone'

class Mods_And_Admin_Only_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # user has joined the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        mention = member.mention
        guild = member.guild
        embed_welcome_message = discord.Embed(title=str("***New User Joined***"), colour=0x68FF33,
                                      description=str(f'{mention} joined to the {guild} :tuilip: :cherries: :shaved_ice: ').format(mention = member.mention))
        embed_welcome_message.set_thumbnail(url=f"{member.avatar_url}")
        embed_welcome_message.set_author(name=f"{member.name}", icon_url=f"{member.guild.icon_url}")
        embed_welcome_message.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        embed_welcome_message.timestamp = datetime.datetime.utcnow()
        embed_welcome_message.add_field(name=str('User ID'), value=f'{member.id}')
        embed_welcome_message.add_field(name=str('User Name '), value=f'{member.display_name}')
        embed_welcome_message.add_field(name=str('Server Name'), value=f'{guild}')
        embed_welcome_message.add_field(name=str('User Serial'), value=f'{len(list(guild.members))}')
        embed_welcome_message.add_field(name=str('Created at'), value=member.created_at.strftime("%a, %d, "))
        role = get(member.guild.roles, name=probationary)
        await member.add_roles(role)
        for channel in member.guild.channels:
            if (str(channel) == "introduce-yourself"):
                await channel.send(embed=embed_welcome_message)



    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed_welcome_message = discord.Embed(title="Welcome to historic-ly",
                                      description='Greetings from Historic-ly Maeven',
                                      color=discord.Colour.green())
        mention = member.mention
        guild = member.guild
        embed_welcome_message = discord.Embed(title=str("***New User Joined***"), colour=0x68FF33,
                                      description=str(f'{mention} joined to the {guild} :tuilip: :cherries: :shaved_ice: ').format(mention = member.mention))
        embed_welcome_message.set_thumbnail(url=f"{member.avatar_url}")
        embed_welcome_message.set_author(name=f"{member.name}", icon_url=f"{member.guild.icon_url}")
        embed_welcome_message.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        embed_welcome_message.timestamp = datetime.datetime.utcnow()
        embed_welcome_message.add_field(name=str('User ID'), value=f'{member.id}')
        embed_welcome_message.add_field(name=str('User Name '), value=f'{member.display_name}')
        embed_welcome_message.add_field(name=str('Server Name'), value=f'{guild}')
        embed_welcome_message.add_field(name=str('User Serial'), value=f'{len(list(guild.members))}')
        embed_welcome_message.add_field(name=str('Created at'), value=member.created_at.strftime("%a, %d, "))
        role = get(member.guild.roles, name=probationary)
        await member.add_roles(role)
        for channel in member.guild.channels:
            if (str(channel) == "introduce-yourself"):
                await channel.send(embed=embed_welcome_message)

    @commands.command()
    async def getusers(self, ctx):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        #if message.channel.is_private or discord.utils.get(message.author.roles, name="Admin"):
        if message.content.startswith('.getusers'):
            embed_message = discord.Embed(title="Current Users",
                                          description = 'List of all users currently in server',
                                          color = discord.Colour.green())
            embed_message_bots = discord.Embed(title="Bots",
                                               description = "List of All Registered Bots on this server",
                                               color = discord.Color.red())
            embed_message_mods = discord.Embed(title="Mods",
                                               description = "List of All Mods on this server",
                                               color = discord.Color.blue())
            embed_message_inactive= discord.Embed(title="List of inactive users",
                                               description = "List of inactive users on this server",
                                               color = discord.Color.blue())
            embed_message_prev= discord.Embed(title="List of previous users",
                                               description = "List of All previous users on this server",
                                               color = discord.Color.blue())
            embed_message_bots.set_footer(text='All registered bots')
            embed_message.set_footer(text='All current Users')
            #embed_message.set_image(url='https://twitter.com/historic_ly/photo')
            #embed_message.set_author(name='Author Name', icon_url='https://twitter.com/historic_ly/photo')
            guild = message.guild #name of server object
            members=guild.members
            inlineVal = False
            headCountBots= 0
            headCountMembers = 0
            headCountMods = 0
            role_names = []
            async with message.channel.typing():
                for member in members:
                    headCountBots = headCountBots + 1
                    if inlineVal == False:
                        inlineVal = True
                    else:
                        inlineVal = False
                    bot= 'No'
                    if (member.bot):
                        headCountBots = headCountBots + 1
                        bot = 'Yes'
                    embed_message.add_field( name=str(f'[{member.id}]'), value=f'name : [{member.name}], highest role : [{member.top_role.name}], bot : [{bot}]\n\u200b\n\u200b', inline = inlineVal)
                    #yield member
                embed_message.add_field(name=f'Total users', value=str(len(members)), inline = False)
                #embed_message.add_field(name=f'Total mods', value=str(headCountMembers), inline=False)
                #embed_message.add_field(name=f'Total bots', value=str(headCountBots), inline=False)
                await message.channel.send(embed=embed_message)


    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_top_role(self, ctx, *, member: discord.Member=None):
        """Simple command which shows the members Top Role."""
        if member is None:
            member = ctx.author
        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')


    @commands.command(aliases=['roles', 'current_roles'])
    async def getalluserroles(ctx):
        ctx.send(f"Message from Maeve: \`.getalluserroles command: Not yet ready still in testing")

    @commands.command()
    async def getregisteredmembers(self, ctx, arg=' '):
        embed_message = discord.Embed(title="Current Registered Users",
                                      description='List of all users currently in server',
                                      color=discord.Colour.green())
        embed_message.set_footer(text='All registered users command')
        if (len(ctx.message.attachments) == 0):
            embed_message.add_field(name=str(f'MAEVE SAYS: '),value=f'User command Error',inline=False)
            embed_message.add_field(name=str(f'Command Usage:'), value=f'Attach the csv file, then type ***\'.getregisteredmembers\'***', inline=False)
        else:
            attachment_url = ctx.message.attachments[0].url
            file_request = requests.get(attachment_url)
            await ctx.send(f'Message from Maeve: \`checking admin\'s csv file, please stand by.....`')
            # process_csv_attachment(file_request)
            #file_content = file_request.content
            #file_content = file_content.replace(b'\r', b'')
            #print(file_content)
            #process_csv_attachment(file_content)
        await ctx.send(embed=embed_message)


    '''
    @commands.command()
    async def kickuser(self, ctx, member: discord.Member, *, reason=None):
        ctx.send(f"Message from Maeve: \`.kickuser command: Not yet ready still in testing")
        #await member.ban(reason=reason)

    @commands.command()
    async def kickusers(self, ctx, member: discord.Member, *, reason=None):
        ctx.send(f"Message from Maeve: \`.kickusers command: Not yet ready still in testing")
        #await member.ban(reason=reason)

    @commands.command()
    async def banuser(self, ctx, member: discord.Member, *, reason=None):
        ctx.send(f"Message from Maeve: \`.kickusers command: Not yet ready still in testing")
        #await member.ban(reason=reason)

    @commands.command()
    async def banusers(self, ctx, member: discord.Member, *, reason=None):
        ctx.send(f"Message from Maeve: \`.kickusers command: Not yet ready still in testing")
        #await member.ban(reason=reason)

    @commands.command()
    async def scanusers(self, ctx, member: discord.Member, *, reason=None):
        #await member.ban(reason=reason)
        ctx.send(f"Message from Maeve: \`.scanusers command: Not yet ready still in testing")

    @commands.command()
    async def verifyuser(self, ctx, member: discord.Member, *, reason=None):
        ctx.send(f"Message from Maeve: \`.verifyuser command: Not yet ready still in testing")

    @commands.command()
    async def whoareyou(self, ctx, member: discord.Member, *, reason=None):
        ctx.send(f"Message from Maeve: \`.whoareyou command: Not yet ready still in testing")

    @commands.command()
    async def checkvalidusers(self, ctx, member: discord.Member, *, reason=None):
        ctx.send(f"Message from Maeve: \`.checkvaliduser command: Not yet ready still in testing")

    @commands.command()
    async def whojoined(self, ctx, member: discord.Member, *, reason=None):
        ctx.send(f"Message from Maeve: \`.whojoined command: Not yet ready still in testing")

    @commands.command()
    async def findpreviousUsers(self, ctx, member: discord.Member, *, reason=None):
        ctx.send(f"Message from Maeve: \`.findpreviousUsers command`: Not yet ready still in testing")
    '''
def setup(client):
    client.add_cog(Mods_And_Admin_Only_Commands(client))


'''
    @commands.command()
    async def getpaiddusers(self, ctx, arg=' '):
        attachment_url = ctx.message.attachments[0].url
        file_request = requests.get(attachment_url)
        await ctx.send('Bounce_checker: `checking admin\'s csv file, please stand by.....`')
        # process_csv_attachment(file_request)
        file_content = file_request.content
        file_content = file_content.replace(b'\r', b'')
        print(file_content)
        #process_csv_attachment(file_content)
'''