#/usr/bin/env python3
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
# from ec2_metadata import ec2_metadata


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('DISCORD_CHANNEL_TEST')

#SERVER=ec2_metadata.public_hostname
SERVER='test'

#client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
#    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(f'guilds: {bot.guilds}')
    guild = discord.utils.find(lambda g: g.name == 'ca', bot.guilds)
    channel = discord.utils.find(lambda c: c.name == 'bot-spam', guild.text_channels)

#    await channel.send(content='👀')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
 
bot.run(TOKEN)

