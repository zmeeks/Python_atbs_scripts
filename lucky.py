#! /usr/bin/env python3
#  lucky.py -- opens several Google search results -- pg. 249
#  Usage:	./lucky.py <search_word_1> <search_word_2> . . . <search_word_N>

"""
README:
Automate The Boring Stuff Python (Ch. 11 -- pg 248) Script
copied by Z Meeks 9/28/17

This script opens the first 7 Google results in new tabs (or less if there are not 7 results)
"""

import requests, sys, webbrowser, bs4

print('Googling...')	# display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(7, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))