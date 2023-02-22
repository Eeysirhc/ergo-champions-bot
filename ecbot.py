##############################
# Author: eeysirhc
# Date written: 2023-02-21
# Last updated: 
##############################

# LOAD PYTHON MODULES
import os 
from dotenv import load_dotenv 
load_dotenv()

import pandas as pd 
pd.set_option('max_colwidth', None)

import tabulate
import discord 
from discord.ext import commands 

# DISCORD CONFIG
intents = discord.Intents().all()
client = commands.Bot(command_prefix = '.', intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

# EVENTS
## BOT STATUS
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity = discord.Game("in Sigmahaven"))

## CHAMPIONS LOOKUP
seasons_data = {
	'1': "rarity_s1.csv",
	'2': "rarity_s2.csv"
}

### LOOKUP SEASONS CSV FILE
def seasons_lookup(season=''):
	season_filter = seasons_data[season]
	df = pd.read_csv(season_filter)
	df['Champion:'] = df['Champion:'].astype('str')
	return(df)

### LOOKUP SPECIFIC CHAMPION
def champions_lookup(df_seasons, champion_id):
	df = df_seasons[df_seasons['Champion:'] == champion_id]
	df = df.squeeze().to_string()
	return(df)

### JOIN SEASONS & CHAMPIONS LOOKUP FUNCTION
def ergo_champs(ec_season, ec_id):
	df_seasons = seasons_lookup(ec_season)
	df_champions = champions_lookup(df_seasons, ec_id)
	return(df_champions)

@client.command()
async def ec(ctx, id_season, id_champion):
    response = ergo_champs(id_season, id_champion)
    embed = discord.Embed(title = "Ergo Champions")
    embed.add_field(name = "Rarity Chart", value=(response), inline=True)
    await ctx.send(embed=embed)

# EXECUTE
client.run(TOKEN)
