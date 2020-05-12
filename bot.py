#/usr/bin/env python3
import os
import random
import discord
import emojis
from discord.ext import commands
from dotenv import load_dotenv

from factorio_rcon import RCONClient

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('DISCORD_CHANNEL_TEST')
FACTORIO_RCON_PWD = os.getenv('FACTORIO_RCON_PWD')
FACTORIO_SERVER = 'localhost'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'guilds: {bot.guilds}')
    guild = discord.utils.find(lambda g: g.name == 'ca', bot.guilds)
    channel = discord.utils.find(lambda c: c.name == 'bot-spam', guild.text_channels)
#    await channel.send(content='👀')


@bot.command(name='emoji', help='Responds with a random emoji')
async def command_emoji(ctx):
    response = str(''.join([random.choice(emojis.db.utils.db.EMOJI_DB).emoji for x in range(3)]))
    await ctx.send(response)


class FactorioCategory(commands.Cog):
    """
    Bot commands for interacting with Factorio server
    """
    @bot.command(name='players', help='List of players in the game')
    async def command_players(ctx):
        rcon = RCONClient(FACTORIO_SERVER, 27016, FACTORIO_RCON_PWD)
        response = rcon.send_command('/players')
        await ctx.send(response)

    @bot.command(name='admins', help='List of admins in the game')
    async def command_admins(ctx):
        rcon = RCONClient(FACTORIO_SERVER, 27016, FACTORIO_RCON_PWD)
        response = rcon.send_command('/admins')
        await ctx.send(response)

    @bot.command(name='seed', help='Prints starting map seed')
    async def command_seed(ctx):
        rcon = RCONClient(FACTORIO_SERVER, 27016, FACTORIO_RCON_PWD)
        response = rcon.send_command('/seed')
        await ctx.send(response)

    @bot.command(name='time', help='Prints info about how old the map is')
    async def command_time(ctx):
        rcon = RCONClient(FACTORIO_SERVER, 27016, FACTORIO_RCON_PWD)
        response = rcon.send_command('/time')
        await ctx.send(response)

    @bot.command(name='version', help='Prints the current game version')
    async def command_version(ctx):
        rcon = RCONClient(FACTORIO_SERVER, 27016, FACTORIO_RCON_PWD)
        response = rcon.send_command('/version')
        await ctx.send(response)

    @bot.command(name='ip', help='Prints public hostname of the factorio server')
    async def command_version(ctx):
        from ec2_metadata import ec2_metadata
        response = f'{ec2_metadata.public_hostname} is the ip!'
        print(response)
        await ctx.send(response)


    # @bot.command(name='rcon', help='Send rcon command to factorio server')
    # async def command_rcon(ctx):
    #     rcon = RCONClient(FACTORIO_SERVER, 27016, FACTORIO_RCON_PWD)
    #     response = rcon.send_command('/')
    #     await ctx.send(response)


class BotCategory(commands.Cog):
    """Category documentations"""

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong"""
        await ctx.send(":ping_pong: Pong!")
        print("user has pinged")

bot.add_cog(BotCategory())

bot.run(TOKEN)
