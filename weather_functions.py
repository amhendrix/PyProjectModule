import json
import requests
import argparse
from geopy.geocoders import Nominatim
from urllib.parse import urlencode
from datetime import datetime



#Function to get the grid coordinates for a location based on city, state, and zipcode
def get_grid_coordinates(city, state, zipcode):
    location = f"{city}, {state} {zipcode}"
    geolocator = Nominatim(user_agent="weather")
    location_info = geolocator.geocode(location)

    if not location_info:
        print(f"Could not find location for {location}")
        return None, None
    lattitude, longitude = location_info.latitude, location_info.longitude
    base_url = url = "https://api.weather.gov/points/"
    headers = {
                    "User-Agent": "MyWeatherApp/0.1 (ahendrickson@comcast.net)"
            }
    url = f"{base_url}{lattitude},{longitude}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        gridX = data.get("properties", {}).get("gridX")
        gridY = data.get("properties", {}).get("gridY")
        grid_coordinates = data.get("properties", {}).get("gridId")
        return grid_coordinates , gridX , gridY # return the grid coordinates and the gridX and gridY ie. ('GSP', '80', '100')
    
    except requests.exceptions.RequestException as e:
        print(f"Error getting grid coordinates: {e}")
        return None, None, None
    
# get forecastHourly - forecast for hourly periods over the next seven days and return the data dictionary
def get_forecast_hourly(office, gridX, gridY):

    base_url = 'https://api.weather.gov/gridpoints/'
    url = f'{base_url}{office}/{gridX},{gridY}/forecast/hourly'# the /forecast is for 12h periods over the next seven days
    headers = {
                    "User-Agent": "MyWeatherApp/0.1 (ahendrickson@comcast.net)"
    }
    response = requests.get(url)
    if response.status_code == 200:
    
        # Convert JSON to Python dictionary
        data_dict = response.json()
        return data_dict
    else: 
        print(f"Error getting hourly forecast: {response.status_code}")
        return None

# get forecast - forecast for 12h periods over the next seven days and return the data dictionary
def get_forecast(office, gridX, gridY):

    base_url = 'https://api.weather.gov/gridpoints/'
    url = f'{base_url}{office}/{gridX},{gridY}/forecast'# the /forecast is for 12h periods over the next seven days
    headers = {
                    "User-Agent": "MyWeatherApp/0.1 (ahendrickson@comcast.net)"
    }
    response = requests.get(url)
    if response.status_code == 200:
    
        # Convert JSON to Python dictionary
        data_dict = response.json()
        return data_dict
    else: 
        print(f"Error getting forecast: {response.status_code}")
        return None

# get forecastGridData - raw forecast data over the next seven days
def get_forecast_grid_data(office, gridX, gridY):


    base_url = 'https://api.weather.gov/gridpoints/'
    url = f'{base_url}{office}/{gridX},{gridY}/forecast/Grid/Data'# the /forecast is for 12h periods over the next seven days
    headers = {
                    "User-Agent": "MyWeatherApp/0.1 (ahendrickson@comcast.net)"
    }
    response = requests.get(url)
    if response.status_code == 200:
    
        # Convert JSON to Python dictionary
        data_dict = response.json()
        return data_dict  
    else:
        print(f"Error getting forecast grid data: {response.status_code}")
        return None  

# print the  hourly forecast
def print_forecast_hourly(data_dict, city, state, zipcode):    
        print(f'The weather forecast for {city}, {state} {zipcode} is as follows:\n')
        #print(data_dict)
        if 'periods'in data_dict.get('properties', {}):
            for period in data_dict['properties']['periods']:
       
                 # Format the start time
                start_time_str = period.get('startTime', 'N/A')
                start_time = datetime.fromisoformat(start_time_str)
                formatted_start_time = start_time.strftime('%Y-%m-%d %I:%M:%S %p')

                # Format the end time
                end_time_str = period.get('endTime', 'N/A')
                end_time = datetime.fromisoformat(end_time_str)
                formatted_end_time = end_time.strftime('%Y-%m-%d %I:%M:%S %p')

                print(f"Start Date and Time:  {formatted_start_time}")
                print(f"End Date and Time:  {formatted_end_time}")
                print(f"Tempurature:  {period.get('temperature', 'N/A')} {period.get('temperatureUnit', 'N/A')}")
                print(f"Wind Speed:  {period.get('windSpeed', 'N/A')} ")
                print(f"Wind Direction:  {period.get('windDirection', 'N/A')}") 
                print(f"Short Forecast:  {period.get('shortForecast', 'N/A')}")
                print('-' * 30)
       
        else:
            print("No data found for hourly forecast")

# print the forecast
def print_forecast(data_dict, city, state, zipcode):  
        print(f'The weather forecast for {city}, {state} {zipcode} is as follows:\n')
        #print(data_dict)
        if 'periods'in data_dict.get('properties', {}):
            for period in data_dict['properties']['periods']:
       
                 # Format the start time
                start_time_str = period.get('startTime', 'N/A')
                start_time = datetime.fromisoformat(start_time_str)
                formatted_start_time = start_time.strftime('%Y-%m-%d %I:%M:%S %p')

                # Format the end time
                end_time_str = period.get('endTime', 'N/A')
                end_time = datetime.fromisoformat(end_time_str)
                formatted_end_time = end_time.strftime('%Y-%m-%d %I:%M:%S %p')
                print(f"Period:  {period.get('name', 'N/A')}")
                print(f"Start Date and Time:  {formatted_start_time}")
                print(f"End Date and Time:  {formatted_end_time}")
                print(f"Tempurature:  {period.get('temperature', 'N/A')} {period.get('temperatureUnit', 'N/A')}")
                print(f"Wind Speed:  {period.get('windSpeed', 'N/A')} ")
                print(f"Wind Direction:  {period.get('windDirection', 'N/A')}") 
                print(f"Short Forecast:  {period.get('shortForecast', 'N/A')}")
                print(f"Detailed Forecast:  {period.get('detailedForecast', 'N/A')}")
                print('-' * 30)
       
        else:
            print("No data found for hourly forecast")

# print the forecast_grid_data(data_dict, city, state, zipcode):
#def print_forecast_grid_data(data_dict, city, state, zipcode):  
        print(f'The weather forecast for {city}, {state} {zipcode} is as follows:\n')
        #print(data_dict)
        if 'periods'in data_dict.get('properties', {}):
            for period in data_dict['properties']['periods']:
       
                 # Format the start time
                start_time_str = period.get('startTime', 'N/A')
                start_time = datetime.fromisoformat(start_time_str)
                formatted_start_time = start_time.strftime('%Y-%m-%d %I:%M:%S %p')

                # Format the end time
                end_time_str = period.get('endTime', 'N/A')
                end_time = datetime.fromisoformat(end_time_str)
                formatted_end_time = end_time.strftime('%Y-%m-%d %I:%M:%S %p')

                print(f"Start Date and Time:  {formatted_start_time}")
                print(f"End Date and Time:  {formatted_end_time}")
                print(f"Tempurature:  {period.get('temperature', 'N/A')} {period.get('temperatureUnit', 'N/A')}")
                print(f"Wind Speed:  {period.get('windSpeed', 'N/A')} ")
                print(f"Wind Direction:  {period.get('windDirection', 'N/A')}") 
                print(f"Short Forecast:  {period.get('shortForecast', 'N/A')}")
                print('-' * 30)
       
        else:
            print("No data found for hourly forecast")
         
        print(f'The weather forecast for {city}, {state} {zipcode} is as follows:\n')
        #print(data_dict)
        if 'periods'in data_dict.get('properties', {}):
            for period in data_dict['properties']['periods']:
       
                 # Format the start time
                start_time_str = period.get('startTime', 'N/A')
                start_time = datetime.fromisoformat(start_time_str)
                formatted_start_time = start_time.strftime('%Y-%m-%d %I:%M:%S %p')

                # Format the end time
                end_time_str = period.get('endTime', 'N/A')
                end_time = datetime.fromisoformat(end_time_str)
                formatted_end_time = end_time.strftime('%Y-%m-%d %I:%M:%S %p')
                print(f"Period:  {period.get('name', 'N/A')}")
                print(f"Start Date and Time:  {formatted_start_time}")
                print(f"End Date and Time:  {formatted_end_time}")
                print(f"Tempurature:  {period.get('temperature', 'N/A')} {period.get('temperatureUnit', 'N/A')}")
                print(f"Wind Speed:  {period.get('windSpeed', 'N/A')} ")
                print(f"Wind Direction:  {period.get('windDirection', 'N/A')}") 
                print(f"Short Forecast:  {period.get('shortForecast', 'N/A')}")
                print(f"Detailed Forecast:  {period.get('detailedForecast', 'N/A')}")
                print('-' * 30)
       
        else:
            print("No data found for forecast")

            