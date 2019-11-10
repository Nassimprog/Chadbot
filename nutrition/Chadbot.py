# Discord modules
#   <<<< Modules use was inspired by Youtube video: "https://www.youtube.com/watch?v=nomK9TIuxwM"
import discord
import random
import asyncio
from discord.ext import commands
from random import randint

# Our modules
from API import recipeInfo
from API import nutInfo

from foodAPI import foodRecipe
from messageRecognition import Recognition
from googleNearestPlacesAPI import NearestPlace

from mainF import searchByIngredient



# Set command prefix
client = commands.Bot(command_prefix = '.')  # <<<< Prefix setting inspired by: "https://www.youtube.com/watch?v=nW8c7vT6Hl4" although not utilized.


###### Standard Functions #######

# Bot is ready.
@client.event               # <<<< Basic on_ready fucntion "https://www.youtube.com/watch?v=nW8c7vT6Hl4"
async def on_ready():
    print('Bot is ready!')

# Member Joined channel.
@client.event
async def on_member_join(member):
    print('{member} has joined the server!')

# Member Left channel.
@client.event
async def on_member_remove(member):
    print('{member} has left the server!')



##### On UserMessage ######

# User Message Events.
@client.event
async def on_message(message):          # <<<< on_message function dicovered from: "https://www.youtube.com/watch?v=XjfxYfKFXO8&t=716s"
  
    userMessage = message.content
    
    # Check if the user wants recipe.
    if '.recipe' in userMessage:

        # Get rid of the front part, and send Reply.
        myList = foodRecipe(Recognition(userMessageModified))

        # Show Bots recommendations (Messages)
        await message.channel.send('**Recipe name:**')
        await message.channel.send('~ ' + myList[0])

        # DISPLAY INGREDIENTS
        await message.channel.send('___________')
        await message.channel.send('**List of ingredients:**')
        for i in range(3):
            await message.channel.send('~ ' + myList[1][i])

        # Display WebPage
        await message.channel.send('...')
        await message.channel.send('___________')
        await message.channel.send('**For full list visit:** ' + myList[2])

    # Check if user wants location.
    if '.location' in userMessage:
        userMessageModified = userMessage[10:]

        # Get the list with Names and Addresses of the places.
        myList = NearestPlace(userMessageModified)

        # Separete Names from Addresses.
        myNameList = myList[0]
        myAddressList = myList[1]

        # Print them out back to user.
        await message.channel.send('*** Here are 3 nearest locations***')
        for i in range(3):
            await message.channel.send('___________')
            await message.channel.send('~ ***Name of the place:*** ' + myNameList[i])
            await message.channel.send('~ ***Address of the place:*** ' + myAddressList[i])

    # Display Nutrition.
    if '.nutrition' in userMessage.lower():
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

    # Display Random Surprise Recipe
    if '.surprise' in userMessage.lower():
        RNG = random.randint(0, 148)
        UserMessage = ('recipe ' + str(RNG))
        await message.channel.send('recipe ' + str(RNG))

    # Display Cocktails
    if '.cocktailIngredient' in userMessage:
        userMessageModified = userMessage[20:]

        await message.channel.send('**Cocktails found for you.**')
        await message.channel.send('___________')
        
        myList = searchByIngredient(Recognition(userMessageModified))

        await message.channel.send('~' + myList[0])
        await message.channel.send('~' + myList[1])
        

# Run bot with this ID
client.run('NjMxNDk2NTc1OTMxMTIxNjk0.XZ4SDQ.GAkS4ucOyN9v5Dd1617tMr-EzDo')
