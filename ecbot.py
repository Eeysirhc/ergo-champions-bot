##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-09-05
##############################

# LOAD PYTHON MODULES
import os
import random
from dotenv import load_dotenv 
load_dotenv() 

import pandas as pd 
import champions as ch 
import discord
from discord.ext import commands

# CONFIG
client = commands.Bot(command_prefix = '/')
TOKEN = os.getenv("DISCORD_TOKEN")

# EVENTS
## BOT STATUS
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity = discord.Game("in Sigmahaven"))

## CHAMPIONS LOOKUP
@client.command()
async def ec(ctx, id_lookup):
    response = ch.champ(id_lookup)
    embed = discord.Embed(title = "Rarity Chart")
    embed.add_field(name = "Results", value=(response), inline=True)
    await ctx.send(embed=embed)

# EXECUTE
client.run(TOKEN)

