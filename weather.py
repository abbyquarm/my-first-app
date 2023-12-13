from iPython.core.display import HTML
import pgeocode
from pgeocode import Nominatim
import requests
import json

def display_forecast(zip_code, country_code="US"):
    ''' Shows the seven day forecast for the inputted zip code

    Parameters:
        country_code (string) is valid country code. Default value is set to "US"

        zip_code (string) is a valid US zip code


    '''

    nomi = Nominatim(country_code)
    geo = nomi.query_postal_code(zip_code)
    latitude = geo["latitude"]
    longitude = geo["longitude"]


    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(request_url)

    parsed_response = json.loads(response.text)

    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    
    
    #print(forecast_response.status_code)
    parsed_forecast_response = json.loads(forecast_response.text)

    periods = parsed_forecast_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period["isDaytime"] == True]