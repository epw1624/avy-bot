# bot actions related to interaction with the server go here
# this file acts as an interface between the server and commands.py

import discord
import commands
import os
from bot import Bot

COMMANDS = ["forecast", "set_home", "home"]
FUNCTIONS = [commands.forecast, commands.set_home, commands.home]

client = discord.Client(intents=discord.Intents(messages=True, message_content=True, emojis=True, emojis_and_stickers=True))
bot = Bot()

@client.event
async def on_ready():
    print("Bot is logged in")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!avy-bot"): # all bot commands will start with !avy-bot
        # split the input into the command and its arguments
        input = message.content.split(' ')
        command = input[1]
        index = COMMANDS.index(command)

        if len(input) == 4:
            bot_message = FUNCTIONS[index](input[2], input[3], bot) #calls the according function

        elif len(input) == 2:
            bot_message = FUNCTIONS[index](bot)

        await message.channel.send(bot_message)


client.run(os.getenv('SECRET_KEY'))


