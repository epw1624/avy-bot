# all bot actions that aren't strictly I/O in the server go here

from get_forecast import get_current_forecast, build_forecast
import discord

client = discord.Client(intents=discord.Intents(messages=True, emojis=True, emojis_and_stickers=True))

def forecast(lat, long):
    """
    Takes the latitude and longitude from a forecast command and returns a Forecast object
    """
    json_forecast = get_current_forecast(lat, long)
    forecast = build_forecast(json_forecast)
    return forecast

def print_forecast(forecast):
    """
    helper method for the forecast command
    takes Forecast obj and generates a string as the message to be returned by bot
    forecast: a Forecast object
    """
    # find emojis
    message = "{highlight}\nAlpine: {alpine}"






