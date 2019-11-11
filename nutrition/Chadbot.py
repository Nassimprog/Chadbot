# Discord modules
#   <<<< Modules use was inspired by Youtube video: "https://www.youtube.com/watch?v=nomK9TIuxwM"
import discord
import random
import asyncio
from discord.ext import commands
from random import randint

# Our modules
from foodAPI import *
from messageRecognition import Recognition
from googleNearestPlacesAPI import NearestPlace

from mainF import *



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
  
    # Check if the message is from user.
    if message.author != client.user:

        # Get the users message.
        userMessage = message.content
        userMessage = userMessage.lower()  # avoids case sensitivity
        
        # Check if the user wants recipe.
        if 'recipe' in userMessage:
            userMessageModified = userMessage[7:]
        

            # Get rid of the front part, and send Reply.
            myList = foodRecipe(Recognition(userMessageModified))

            # Show Bots recommendations (Messages)
            await message.channel.send('**Recipe name:**')
            await message.channel.send('~ ' + myList[0])

            # DISPLAY INGREDIENTS
            await message.channel.send('___________')
            await message.channel.send('**List of ingredients:**')
            
            lenOfMyList = len(myList[1])

            if lenOfMyList >= 3:
                    lenOfMyList = 3

            for i in range(lenOfMyList):
                await message.channel.send('~ ' + myList[1][i])

            # Display WebPage
            await message.channel.send('...')
            await message.channel.send('___________')
            await message.channel.send('**For full list visit:** ' + myList[2])

        # Check if user wants location.
        if 'location' in userMessage:
            userMessageModified = userMessage[9:]

            # Get the list with Names and Addresses of the places.
            myList = NearestPlace(userMessageModified)

            lenOfMyList = len(myList[1])

            if lenOfMyList >= 3:
                    lenOfMyList = 3

            # Separete Names from Addresses.
            myNameList = myList[0]
            myAddressList = myList[1]

            # Print them out back to user.
            await message.channel.send('*** Here are 3 nearest locations***')
            for i in range(lenOfMyList):
                await message.channel.send('___________')
                await message.channel.send('~ ***Name of the place:*** ' + myNameList[i])
                await message.channel.send('~ ***Address of the place:*** ' + myAddressList[i])

          # Display Nutrition.
       
        # Display nutritions
        if 'nutrition' in userMessage:
            userMessageModified = userMessage[9:]
            nDisplay = nutInfo(userMessageModified)
            nLIST = len(nDisplay[2])
            ''' To display the nutrition '''
            await message.channel.send(str(nDisplay[0]) + "\n")
            for i in range(nLIST):
                await message.channel.send('This is: ' + str(nDisplay[2][i]) + ".\n")
            await message.channel.send('This has: ' + str(nDisplay[1]) + " kcal (calories)." + "\n")
            await message.channel.send('This has: ' + str(nDisplay[3]) + " grams of fat." + "\n")
            await message.channel.send('This has: ' + str(nDisplay[4]) + " grams of sugar." + "\n")
            await message.channel.send('This has: ' + str(nDisplay[5]) + " grams of carb." + "\n")
            await message.channel.send('This has: ' + str(nDisplay[6]) + " grams of protein." + "\n")
            
            print(userMessage)

        if 'surprise' in userMessage.lower():
                ''' to search for a recipe by number '''
                RNG = random.randint(0, 148)

                rDisplay = foodRecipe(str(RNG))

                rLIST = len(rDisplay[1])
                if rLIST >= 3:
                    rLIST = 3
                print(rLIST)
                await message.channel.send('════ ≪ °❈ Name ❈° ≫ ════\n')

                await message.channel.send(rDisplay[0])

                await message.channel.send('════ ≪ °❈ Ingredients ❈° ≫ ════\n')
                
                for i in range(rLIST):  # to display the ingredients in a readable listnagain
                    await message.channel.send(rDisplay[1][i])
                
                await message.channel.send('════ ≪ °❈ Link ❈° ≫ ════\n')
                await message.channel.send(rDisplay[2])

        # Display Cocktails
        if 'cocktailingredient' in userMessage:
            userMessageModified = userMessage[19:]

            await message.channel.send('**Cocktails found for you.**')
            await message.channel.send('___________')
            
            myList = searchByIngredient(userMessageModified)

            await message.channel.send('~' + myList[0])
            await message.channel.send('~' + myList[1])
            
        if 'cocktailname' in userMessage:
            userMessageModified = userMessage[13:]

            await message.channel.send('**Cocktail.**')
            await message.channel.send('___________')

            myList = searchByName(userMessageModified)

            for i in range(6):

                await message.channel.send('~' + myList[i])

        if 'randomcocktail' in userMessage:
            userMessageModified = userMessage[14:]

            await message.channel.send('**Random Cocktail.**')
            await message.channel.send('___________')
            await message.channel.send('~' + randomCocktail())

# Run bot with this ID
client.run('NjMxNDk2NTc1OTMxMTIxNjk0.XZ4SDQ.GAkS4ucOyN9v5Dd1617tMr-EzDo')
