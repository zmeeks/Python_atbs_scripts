#! /usr/bin/env python3
# umbrella.py - a program that will send me a text if it is forecasted to rain today.

"""
README:
Automate The Boring Stuff Python (Ch. 16 -- pg 385) Project
solved by Z Meeks 10/05/17

Note: 	not yet complete -- need to add automatic scheduling to run this program in the early
		morning, every morning.
Note:	need to replace API_key, location, my_gmail, my_pword, phone_num_email with your correct values
"""

import json, requests, sys, pprint, smtplib
										   
API_key = '********************************' # key for API as generated on openweathermap.org
location = '___ _______' # i.e. 'Los Angeles' -- check your location string against openweathermap.com
my_gmail = '_______@gmail.com' # replace with your valid @gmail login
my_pword = '*************'		# replace with your correct password
phone_num_email = '__________@__________.com' # i.e. 3105552468@messaging.sprintpcs.com'

url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&APPID=%s' % (location, API_key)

# Download the JSON data from OpenWeatherMap.org's API
response = requests.get(url)
response.raise_for_status

# Load JSON data into a Python variable
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData['list']
if w[0]['weather'][0]['main'] == 'Rain':
	print('maybe: RAIN TODAY!!')
	desc = w[0]['weather'][0]['description']
	# Log in to email account
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(my_gmail, my_pword)
	subject = "\n\n" #\n\n = skips subject as blank -- blank bc sending as text message
	body = 	("To: %s \n"
			"Subject: %s" 
			"Bring an umbrella! Rain today -- %s"
		   	) % (phone_num_email, subject, desc)	
	sendmailStatus = smtpObj.sendmail(my_gmail, phone_num_email, body)
	if sendmailStatus != {}:
		print('There was a problem sending rain/umbrella warning')
smtpObj.quit()

