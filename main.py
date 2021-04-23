import discord
import os
import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-lol hello'):
        await message.channel.send('Hello!')
    if message.content.startswith("-build"):
        words = message.content.split();
        if len(words) <2:
            await message.channel.send("Please enter a champion name!")
            return
        if len(words) < 3:
            await message.channel.send("Showing the top pro build for " + words[1].capitalize())
            return
        if len(words) < 4:
            await message.channel.send("Showing the top pro build for " + words[1].capitalize() + " in lane: " + words[2].capitalize())
        

client.run(config.dc_token)