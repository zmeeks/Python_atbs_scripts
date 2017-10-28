#! /usr/bin/env python3
#  quickWeather.py -- Prints the weather for a location from the command line

"""
README:
Automate The Boring Stuff Python (Ch. 14 -- pg 329) Script
copied/solved by Z Meeks 10/04/17

Note:	API has probably changed a bit since book's publication -- had to fix a few things :)
Note:	Need to sign up for API key and replace API_key value with real key
"""

import json, requests, sys, pprint
                                           
API_key = '********************************' # key for API as generated on openweathermap.org

# Compute location from command line arguments
if len(sys.argv) < 2:
	print('Usage:  ./quickWeather.py the location')
	sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&APPID=%s' % (location, API_key)
response = requests.get(url)
response.raise_for_status

# Load JSON data into a Python variable
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData['list']
print('current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])