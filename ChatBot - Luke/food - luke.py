import discord
import random
from discord.ext import commands
import requests
import asyncio
import random

client = commands.Bot(command_prefix = '') 



@client.event
async def on_ready():
    print('Chef Chad has awoken')

@client.event
async def on_message(message):
    if message.content == 'chicken':        #<---If statement so when the user picks 'chicken' from list, it responds 
        await message.channel.send('why not try a chicken madras?')
    elif message.content == 'beef':
        await message.channel.send('try and make a lasagne?' '\n' 'https://www.goodhousekeeping.com/uk/food/recipes/a544697/classic-lasagne-544697/')   #<--- Links user to a web to cook lasagne
    elif message.content == 'lamb':
        await message.channel.send('lamb is a tough one, why not try this:' '\n' '')

    if message.content == 'show me a list of currys please':
        await message.channel.send('here is a website for currys. I recommend the chicken Madras!' '\n' 'https://www.bbcgoodfood.com/recipes/collection/curry')
    

#APIKEY = "APIKEYHERE"




client.run('#insert bot token#')
