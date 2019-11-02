import discord
import random
import asyncio

# My modules
from API import recipeInfo
from API import nutInfo
from discord.ext import commands
from random import randint

###################### Based on Discord Template from : (URL goes here)         In order to turn
#

client = commands.Bot(command_prefix = '.')



@client.event #
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
    
#
########################## END OF ##############



@client.event
async def on_message(message):
  
    userMessage = message.content
    rDisplay = recipeInfo(userMessage)
    
    #nDisplay = str(nutVar)
    # Display Recipe
    # [0] is the name of recipe [1] is the ingredients [2] is url and image [3] is out of range
    if 'recipe' in userMessage.lower():
        #displaying it all on discord
        await message.channel.send('════════════════════ ≪ °❈ Name ❈° ≫ ════════════════════\n')
        
        await message.channel.send(rDisplay[0])
        
        await message.channel.send(rDisplay[2])
        
        await message.channel.send('═══════════════════ ≪ °❈ Ingredients ❈° ≫ ══════════════════\n')
        for i in range(15): # to display the ingredients in a readable list
            await message.channel.send(rDisplay[1][i])
        
        
        
        
    
    # Display Nutrition
    if 'nutrition' in userMessage.lower():
        nDisplay = nutInfo(userMessage)
        await message.channel.send(str(nDisplay[0]) + "\n")
        await message.channel.send(str(nDisplay[1]) + "\n"  )
        await message.channel.send('calories: ' +  str(nDisplay[2]) + " kcal" + "\n")
        for i in range(5):
            await message.channel.send('This is: ' + str(nDisplay[3][i]) + "\n")
        await message.channel.send('This has: ' + str(nDisplay[4]) + " grams of fat" +"\n")
        await message.channel.send('This has: ' + str(nDisplay[5]) + " grams of sugar" +"\n")
        await message.channel.send('This has: ' + str(nDisplay[6]) + " grams of carb" +"\n")
        #await message.channel.send('This recipe has: ' + nDisplay[2] + " grams of fibre" +"\n")
        await message.channel.send('This has: ' + str(nDisplay[7]) + " grams of protein" +"\n")

        
        print(userMessage)


    if 'surprise' in userMessage.lower():
        RNG = random.randint(0, 148)
        UserMessage = ('recipe ' + str(RNG))
        await message.channel.send('recipe ' + str(RNG))


client.run('NjMxNDk2NTc1OTMxMTIxNjk0.XZ4SDQ.GAkS4ucOyN9v5Dd1617tMr-EzDo')