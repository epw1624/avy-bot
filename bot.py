# bot actions related to interaction with the server go here
# this file acts as an interface between the server and commands.py

import discord
import commands
import os

COMMANDS = ["forecast"]
FUNCTIONS = [commands.forecast]

client = discord.Client(intents=discord.Intents(messages=True, emojis=True, emojis_and_stickers=True))

@client.event
async def on_ready():
    print("Bot is logged in")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!avy-bot'): # all bot commands will start with !avy-bot
        # split the input into the command and its arguments
        input = message.content.split(' ')
        command = input[1]
        index = COMMANDS.index(command)
        bot_message=FUNCTIONS[index](input[2], input[3]) #calls the according function

        await message.channel.send(bot_message)


client.run(os.getenv('SECRET_KEY'))

