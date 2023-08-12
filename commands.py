# all bot actions that aren't strictly I/O in the server go here

from get_forecast import get_current_forecast, build_forecast
import discord

client = discord.Client(intents=discord.Intents(messages=True, emojis=True, emojis_and_stickers=True))

EMOJIS = {"low": '�', "moderate": '�', 
          "considerable": '�', "high": '�', 
          "extreme": '⬛', "norating": '❔'}

def forecast(lat, long):
    """
    Takes the latitude and longitude from a forecast command and returns a Forecast object
    """
    json_forecast = get_current_forecast(lat, long)
    forecast = build_forecast(json_forecast)

    # create the string to be returned for the bot to send to server
    bot_message = "{highlight}\nAlpine: {alpine} {alpine_emoji}\n Treeline: {treeline} {treeline_emoji}\n Below Treeline: {below_treeline} {below_treeline_emoji}".format(
        alpine=forecast.alpine, alpine_emoji=EMOJIS[forecast.alpine], treeline=forecast.treeline, 
        treeline_emoji=EMOJIS[forecast.treeline], below_treeline=forecast.below_treeline, 
        below_treeline_emoji=EMOJIS[forecast.below_treeline]
    )

    return bot_message
    
    







