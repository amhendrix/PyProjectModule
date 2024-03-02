import json
import requests
import argparse
#First go at getting weather data from the Weather.gov API

#All urls are working
#url = "https://api.weather.gov"
#url = "https://api.weather.gov/alerts/active/region/AT"
#url = "https://api.weather.gov/alerts/active/area/TN"
#lat = 47.6062
#lon = -122.3321
 #url = "https://api.weather.gov/points/47.6062,-122.3321"
# headers = {
 #   "User-Agent": "MyWeatherApp/0.1 (ahendrickson@comcast.net)"
 #}
#response = requests.get(url, headers=headers)
#Next two lines for future testing 
#state = input("Enter the state abbreviation: ")
#print('ie: WA, OR, CA, etc.')
parser = argparse.ArgumentParser(description="Get the weather forecast for a location")
#parser.add_argument("state", help="The state abbreviation")
#parser.add_argument("city", help="The city name")
#args = parser.parse_args()

url = "https://api.weather.gov/gridpoints/SEW/125,68/forecast/hourly"
#querystring = {"lat":47.6062,"lon":-122.3321}
headers = {
        "User-Agent": "MyWeatherApp/0.1 (ahendrickson@comcast.net)"
    }

response = requests.get(url, headers=headers)
if response.status_code == 200: 
    data = response.json()
    print(json.dumps(data, indent=2))
    #for key, value in data.items():
        #print(key, data[key]) 
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)
#Using the weather api for ninjas API
url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

querystring = {"city":"Asheville","state":"NC","country":"US","units":"imperial","lang":"en","format":"json"}

headers = {
	"X-RapidAPI-Key": "119e51db99mshfbc57f38af04475p1b68eejsn91045bbea6b6",
	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()
    
    for key, value in data.items():
        print(key, data[key])
    
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)
