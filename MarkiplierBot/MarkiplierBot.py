# bot .py
from inspect import getmembers
import os
import discord
import datetime
import time
from discord.ext import commands
from dotenv import load_dotenv

#load variables from .env
load_dotenv()

#discord token and server names
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#variable def
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', intents = intents)

#bot commands

#play audio
@bot.command()
async def play(ctx):
    voice = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe("markiplier.mp3")
    voice.play(source)

#join voice channel
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

#leave voice channel
@bot.command()
async def leave(ctx):
    await ctx.guild.voice_client.disconnect()

#command for hello everybody my name is markiplier
@bot.command()
async def markiplier(ctx):
    #define voice channel and seconds for timer
    channel = ctx.author.voice.channel
    sec = 6

    #connect and play audio
    await channel.connect()
    voice = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe("markiplier.mp3")
    voice.play(source)

    #wait till end of audio then leave
    while sec:
        time.sleep(1)
        sec -= 1

    #leave after timer is up
    await ctx.guild.voice_client.disconnect()

#moderation commands

#run the bot
print("markiplier is connecting...")
bot.run(TOKEN)
