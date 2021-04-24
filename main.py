import discord
import os
import config
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello ') or message.content.startswith('-hello Mei') or message.content.startswith('-hello mc'):
        await message.channel.send('I am asexual')
    if message.content.startswith("-summoner"):
        words = message.content.split();
        if len(words) <2:
            await message.channel.send("Please enter a summoner name!")
        if len(words) > 2:
            await message.channel.send("Incorrect format")
        if len(words) == 2:
            await message.channel.send("https://app.mobalytics.gg/lol/profile/na/" +words[1] +"/overview")


        
    if message.content.startswith("-build"):
        words = message.content.split();
        if len(words) <2:
            await message.channel.send("Please enter a champion name!")
            return
        if len(words) >= 2:
            champ = ""
            for i in range(1, len(words)):
                champ+=words[i]
            page = requests.get("https://probuildstats.com/champion/" + champ)
            soup= BeautifulSoup(page.content, "lxml")
            result = soup.find_all("div", class_="top-players")
            if len(result) == 0:
                await message.channel.send("Could not find top pro builds for this champion. \nPlease refer to  "+ "https://probuildstats.com/champion/"+ words[1])
                return
            summaries = result[0].find_all("div", class_ = "match-summary")
            result = "Builds:\n\n"
            for summary in summaries:
                player = summary.find_all("a",class_="name")[0]
                team = summary.find_all("div",class_="team-name")[0]
             
                result += "Player: " + player.text + ",  Team: " + team.text + "\n"



                skills = summary.find_all("div", class_="summoner-spells");
                skillImgs = skills[0].find_all("img",alt = True)
                result += "Spells: "
                for img in skillImgs:
                    result +=img['alt'].split()[2] + ", "
                    print(img['alt'])
                result +="\n"

                
                items = summary.find_all("div", class_ = "items")
                imgs = items[0].find_all("img", alt = True)
                result += "Items: "
                for img in imgs:
                    result +=img['alt'] + ", "
                    print(img['alt'])
                result += "\n"
                result +="\n"

            
            
            await message.channel.send("Showing the top pro builds for " + champ.capitalize() +"\n" + result +"\nFor more info go to https://probuildstats.com/champion/"+ champ)
          
            return
        

client.run(config.dc_token) #get dc bot token