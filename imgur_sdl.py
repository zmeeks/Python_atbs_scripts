#! /usr/bin/env python3
#  imgur_sdl.py -- imgur search and download -- automated
#  Usage:	./imgur_sdl.py <search_term_1> ... <search_term_k>

"""
README:
Automate The Boring Stuff Python (Ch. 11 -- pg 263) Project
solved by Z Meeks 10/01/17

This script goes to imgur and downloads all of the pictures on the first page
of the search results for a given search parameter in the command line arguments
"""

import sys, time, webbrowser, os, requests, bs4
from selenium import webdriver

print('starting')

browser = webdriver.Firefox()
terms = []
for i in range(1, len(sys.argv)):
	terms.append(sys.argv[i])
search_str = '+'.join(terms)
folder = 'imgur.'+'_'.join(terms)
os.makedirs(folder, exist_ok=True)
browser.get('https://imgur.com/search/score?q='+search_str)
time.sleep(3)
images = browser.find_elements_by_css_selector('a.image-list-link')
img_links = []
for image in images:
	img_links.append(str(image.get_attribute('href')))

for link in img_links:
	try:
		res = requests.get(link)
		soup = bs4.BeautifulSoup(res.text)
		imgElem = soup.select('img')
		print("downloading img from link : " + link)
		img_url = 'http:' + imgElem[0].get('src')
		res = requests.get(img_url)
		res.raise_for_status()
		imageFile = open(os.path.join(folder, os.path.basename(img_url)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		time.sleep(1)
	except:
		print("encountered a GIF")

print('done')

	