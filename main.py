#import required dependicies
import discord
from discord.ext import commands

#import Bot Token
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@client.event
async def on_ready ():
    print("Pot Commands")
    print("---------")

@client.command()
async def rank(ctx):
    await ctx.send("Your current rank is Radiant")
#testing

client.run(os.getenv("MY_KEY"))




