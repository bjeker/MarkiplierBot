# bot .py
import os
from this import d
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

#discord token and server names
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#variable def
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', intents= intents)

#bot commands

#play
@bot.command()
async def play(ctx):
    voice = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe("markiplier.mp3")
    voice.play(source)

#join
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

#leave
@bot.command()
async def leave(ctx):
    await ctx.guild.voice_client.disconnect()

@bot.command()
async def markiplier(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = ctx.voice_client
    source = await discord.FFmpegOpusAudio.from_probe("markiplier.mp3")
    voice.play(source)

#events
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "markiplier":
        channel = message.author.voice.channel
        await channel.connect()
        voice = bot.voice_client
        source = await discord.FFmpegOpusAudio.from_probe("markiplier.mp3")
        voice.play(source)

#run the bot
bot.run(TOKEN)