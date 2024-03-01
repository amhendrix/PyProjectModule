import requests
#First go at getting weather data from the National Weather Service

#All urls are working
#url = "https://api.weather.gov"
#url = "https://api.weather.gov/alerts/active/region/AT"
#url = "https://api.weather.gov/alerts/active/area/TN"
latitude = 47.6062
longitude = -122.3321
url = "https://api.weather.gov/zones?area=TN&type=forecast"
headers = {
    "User-Agent": "MyWeatherApp/0.1 (ahendrickson@comcast.net)"
}
response = requests.get(url, headers=headers)
#Next two lines for future testing 
#state = input("Enter the state abbreviation: ")
#print('ie: WA, OR, CA, etc.')
if response.status_code == 200:
    data = response.json()
    # Process the data here 
    #for key, value in data.items():
        #print(key, data[key])
    print(data['features'][0]['properties'])
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)

#Second go at getting weather data from the National Weather by API Ninjas

"""
url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

querystring = {"city":"Seattle"}

headers = {
	"X-RapidAPI-Key": "119e51db99mshfbc57f38af04475p1b68eejsn91045bbea6b6",
	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()
    # Process the data here 
    for key, value in data.items():
        print(key, data[key])
    
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)
"""