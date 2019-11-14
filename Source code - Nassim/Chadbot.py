# Discord modules
#   <<<< Modules use was inspired by this Youtube video: "https://www.youtube.com/watch?v=nomK9TIuxwM"
import discord
import random
import asyncio
from discord.ext import commands
from random import randint

# Our modules
from API import recipeInfo
from API import nutInfo






# Set command prefix
client = commands.Bot(command_prefix = '.')  # <<<< Prefix setting inspired by: "https://www.youtube.com/watch?v=nW8c7vT6Hl4" although not utilized.


###### Standard Functions ########################################################################

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



##### On UserMessage ###########################################################

# User Message Events.
@client.event
async def on_message(message):          # <<<< on_message function dicovered from: "https://www.youtube.com/watch?v=XjfxYfKFXO8&t=716s"
    if message.author != client.user: # Discord documentation  https://discordpy.readthedocs.io/en/latest/ext/commands/api.html
        userMessage = message.content 
        userMessage = userMessage.lower() 

        
        if 'recipe' in userMessage:      

            rDisplay = recipeInfo(userMessage)
            rLIST = len(rDisplay[1])
            # [0] is the name of recipe [1] is the ingredients [2] is url and image [3] is out of range 
            '''displaying the recipe on discord '''

            await message.channel.send('════════════════════ ≪ °❈ Name ❈° ≫ ════════════════════\n')
        
            await message.channel.send(rDisplay[0])
        
            await message.channel.send('═══════════════════ ≪ °❈ Ingredients ❈° ≫ ══════════════════\n')
            for i in range(rLIST): 
                await message.channel.send(rDisplay[1][i])

            await message.channel.send('═══════════════════ ≪ °❈ For more info... ❈° ≫ ══════════════════\n')
            await message.channel.send(rDisplay[2])

       

        if 'nutrition' in userMessage:
            nDisplay = nutInfo(userMessage)
            nLIST = len(nDisplay[3])

            ''' To display the nutrition '''
            await message.channel.send(str(nDisplay[0]) + "\n")
            await message.channel.send(str(nDisplay[1]) + "\n"  )
            await message.channel.send('calories: ' +  str(nDisplay[2]) + " kcal" + "\n")
            for i in range(nLIST):
                await message.channel.send('This is: ' + str(nDisplay[3][i]) + "\n") #displays health lables in a list
            await message.channel.send('This has: ' + str(nDisplay[4]) + " grams of fat" +"\n")
            await message.channel.send('This has: ' + str(nDisplay[5]) + " grams of sugar" +"\n")
            await message.channel.send('This has: ' + str(nDisplay[6]) + " grams of carb" +"\n")
            await message.channel.send('This has: ' + str(nDisplay[7]) + " grams of protein" +"\n")
        
        

    # Display Random Surprise Recipe
        if 'surprise' in userMessage.lower():
            ''' to search for a recipe by number '''
            RNG = random.randint(0, 148)
            
            rDisplay = recipeInfo(str(RNG))
            rLIST = len(rDisplay[1])
            
            await message.channel.send('════════════════════ ≪ °❈ Name ❈° ≫ ════════════════════\n')
        
            await message.channel.send(rDisplay[0])
        
            await message.channel.send(rDisplay[2])
        
            await message.channel.send('═══════════════════ ≪ °❈ Ingredients ❈° ≫ ══════════════════\n')
            for i in range(rLIST): # to display the ingredients in a readable list again
                await message.channel.send(rDisplay[1][i])


# Run bot with this ID
client.run('BOT TOKEN')
