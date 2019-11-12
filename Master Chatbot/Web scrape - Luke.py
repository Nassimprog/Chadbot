import discord
import random
from discord.ext import commands
import requests
import asyncio
from urllib.request import urlopen
from bs4 import BeautifulSoup       #<---package that allows me to web scrape

client = commands.Bot(command_prefix = '')      #<---removed any prefix so only need to type in certain words to get a response from bot

@client.event
async def on_ready():
    print('Chef Chad has awoken')       #<---used to let the user know if the bot is running correctly


#inspiration from >>> https://www.youtube.com/watch?v=XQgXKtPSzUI&t=658s
myURL = 'https://www.thechefsforum.co.uk/about-us/'     #<---url used for web scraping
@client.event
async def on_message(message):
    if message.content == 'tell me about the chefs forum chad' or message.content == 'whats the forum':
        myClient = urlopen(myURL)       #<---opens a connection with the 
        page_html = myClient.read()
        myClient.close
        pageSoup = BeautifulSoup(page_html, "html.parser")      #<---does the HTML parsing
        aboutUs = pageSoup.find_all("div",{"id":"content"})     #<---spefically finds the location of desired text in HTML site
        for about in aboutUs:    
            about = aboutUs[0]
        await message.channel.send(about.text[0:1753])      #<---range function used to stop the scrape from exceeding 2000 character limit
    if message.content == 'where can i find more?' or message.content == 'cool give me more':
        await message.channel.send('Why here you go:''\n' 'https://www.thechefsforum.co.uk/about-us/')      #<-- used or statatement so more than one phrase can be used
        return                                                                                              #<---Response linked with a link to the website in use
'''  
    if message.content == 'lemme see a pic':
        clientPic = pageSoup.find_all("img"),{"class":"wp-image-6237 size-medium alignright"}
        for picture in clientPic:
            picture = clientPic[0]
            await message.channel.send(picture.img)'''      #<---code that didnt work - tried to get the scraper to take the image and post into Discord Chat


client.run('NjI4MzYyNTM4ODIzNzEyNzg4.XcWzhw.RS8AWHp0y28MAvj4E_A4rdv10iY')


