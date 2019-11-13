import discord
import random
from discord.ext import commands
import requests
import asyncio


#Everything needed in this .py file

client = commands.Bot(command_prefix = '') 

@client.event
async def on_ready():
    print('Chef Chad has awoken')


@client.command(aliases = ['Hi', 'Chad', 'Father?', 'Hello Chad', 'hello chad', 'hello', 'Hello'])      #<---greeting command so when a user inputs one of these, 
async def hi(ctx):                                                                                      #then the bot will respond
    await ctx.channel.send('Hello my friend' + ', ' + ctx.message.author.mention)   #<---responds with a message plus the users name 
    

@client.command(questions = ['are you well', 'how are you'])    #<---command that pciks a random response when certain question is asked
async def how(ctx):
    responses = ['A little under the weather a monster will quench my thirst, make sure its zero though... Absolute zero.', 
'Marvelous! The birds are chirping, and the kyles are punching their walls... The world is bliss.', 'yeahhh im pretty good']
    response = random.choice(responses)
    await ctx.send('well ' + ctx.message.author.mention + ', ' + (response) + '\n' + 'anyways... How can i help you?')

myUrl = 'https://www.thechefsforum.co.uk/category/news/'    #<---the URL

@client.command(link = ['news please', 'news'])     #<---command to link a News website when asking for News
async def news(ctx):
    await ctx.send('Hmm, well the news seems fruitful:' '\n' 'https://www.thechefsforum.co.uk/category/news/')

@client.command(questions = ['you good', 'are you well', 'how are you', 'you okay'])    #<---command that picks a random response when certain question is asked
async def you(ctx):

    responses = ['A little under the weather a monster will quench my thirst, make sure its zero though... Absolute zero.', 
'Marvelous! The birds are chirping, and the kyles are punching their walls... The world is bliss.', 'yeahhh im pretty good'] 
    response = random.choice(responses)     #<---Random function so that the bot responds with one of the choices typed out in the list
    await ctx.send('well ' + ctx.message.author.mention + ', ' + (response) + '\n' + 'anyways... How can i help you?')



client.run('#insert bot token#')
