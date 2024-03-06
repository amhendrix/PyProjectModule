import json
import requests
import argparse
from geopy.geocoders import Nominatim
from urllib.parse import urlencode
from datetime import datetime
from weather_functions import get_grid_coordinates, get_forecast, get_forecast_hourly, print_forecast, print_forecast_hourly
#parser = argparse.ArgumentParser(description="Get the weather forecast for a location")
##parser.add_argument("city", help="The city name")
#args = parser.parse_args()
city = "Asheville"
state = "NC"
zipcode = "28801"


grid_coordinates = get_grid_coordinates({city}, {state}, {zipcode}) # call function and pass the city, state, zipcode
 # create a dictionry of the parameters ie. {'office':'GSP', 'gridX':'80', 'gridY':'100'}
params = {
    'office' : grid_coordinates[0], 
    'gridX'  : grid_coordinates[1],  
    'gridY'  : grid_coordinates[2],  
    }
office = params['office']
gridX = params['gridX']
gridY = params['gridY']

forecast = get_forecast(grid_coordinates[0], grid_coordinates[1], grid_coordinates[2]) # call function and pass the grid coordinates 
print_forecast( forecast, city, state, zipcode) # call function and pass the forecast, city, state, zipcode
forecast_hourly = get_forecast_hourly(grid_coordinates[0], grid_coordinates[1], grid_coordinates[2]) # call function and pass the grid coordinates
print_forecast_hourly( forecast_hourly, city, state, zipcode) # call function and pass the forecast, city, state, zipcode
#forecast_grid_data = get_forecast_grid_data(grid_coordinates[0], grid_coordinates[1], grid_coordinates[2]) # call function and pass the grid coordinates
#print_forecast_grid_data( forecast_grid_data, city, state, zipcode) # call function and pass the forecast, city, state, zipcode
