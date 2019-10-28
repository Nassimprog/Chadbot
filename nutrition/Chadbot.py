import discord
import random
import asyncio

# My modules
from API import recipeInfo
from API import nutInfo
from discord.ext import commands
from random import randint

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_member_join(member):
    print('{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print('{member} has left the server!')





# Set command prefix
client = commands.Bot(command_prefix = '.')

# Events, bot ready check
@client.event
async def on_ready():
    print('Bot is ready.')
    


#userMessage = ""

@client.event
async def on_message(message):
  
    userMessage = message.content
    rDisplay = recipeInfo(userMessage)
    nutVar = nutInfo(userMessage)
    nDisplay = str(nutVar)
    # Display Recipe
    # [0] is the name of recipe [1] is the ingredients [2] is url and image [3] is out of range
    if 'recipe' in userMessage.lower():
        #displaying it all on discord
        await message.channel.send('════════════════════ ≪ °❈ Name ❈° ≫ ════════════════════\n')
        
        await message.channel.send(rDisplay[0])
        
        await message.channel.send(rDisplay[2])
        
        await message.channel.send('═══════════════════ ≪ °❈ Ingredients ❈° ≫ ══════════════════\n')
        for i in range(10): # to display the ingredients in a readable list
            await message.channel.send(rDisplay[1][i])
        
        
        
        
    
    # Display Nutrition
    if 'nutrition' in userMessage.lower():
        
        await message.channel.send(nDisplay)
        print(userMessage)


    if 'surprise' in userMessage.lower():
        RNG = random.randint(0, 148)
        UserMessage = ('recipe ' + str(RNG))
        await message.channel.send('recipe ' + str(RNG))


client.run('NjMxNDk2NTc1OTMxMTIxNjk0.XZ4SDQ.GAkS4ucOyN9v5Dd1617tMr-EzDo')