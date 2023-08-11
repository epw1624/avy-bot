import requests
import json
from forecast import Forecast

def get_current_forecast(lat, long):
    """
    Makes an API call to the Avalanche Canada API for the avalanche forecast at the given coordinates
    lat: latitude
    long: longitude
    returns a JSON object with the results
    """
    query = "https://api.avalanche.ca/forecasts/:lang/products/point?lat={latitude}&long={longitude}".format(latitude=lat, longitude=long)

    response = requests.get(query)

    with open("forecast.json", 'w') as outfile:
        outfile.write(json.dumps(response.json()))

    return response.json()

def decode_forecast(response):
    """
    Interprets the JSON response into a readable avalanche forecast
    response: the JSON response as returned by get_current_forecast
    returns a Forecast object with the data from the response
    """
    # just want highlights until the end of the first paragraph
    print(type(response))
    highlights = response["report"]["highlights"].split('>')[1].split('<')[0] # this is gross
    confidence = response["report"]["confidence"]["rating"]["value"]
    danger_ratings = response["report"]["dangerRatings"][0]["ratings"]

    alpine = danger_ratings["alp"]["rating"]["value"]
    treeline = danger_ratings["tln"]["rating"]["value"]
    below_treeline = danger_ratings["btl"]["rating"]["value"]

    return Forecast(highlights, alpine, treeline, below_treeline, confidence)


# driver code for testing
lat = 50.993293
long = -118.197407

response = get_current_forecast(lat, long)
forecast = decode_forecast(response)
forecast.display()