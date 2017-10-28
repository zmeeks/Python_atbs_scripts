#! /usr/bin/env python3
#  multiDLxcd.py -- Downloads XKCD comics using multiple threads -- pg. 350

"""
README:
Automate The Boring Stuff Python (Ch. 15 -- pg 350) Script
copied by Z Meeks 10/04/17

Note -- this script isn't dynamic as is -- it doesn't handle the constant additions of comics to xkcd;
		one solution would be to use beautifulsoup to first download comics using a single thread 
		starting with the most recent one until we reach a comic whose permanent link has modulo 100 
		== 0, then pass that number W to the multi-thread algo below such that we replace the 1900 in
		"for i in range(0,1900,100)" with a variable that gets passed that number W.
"""

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok = True) 	# stores comics in a folder named 'xkcd'

def downloadXkcd(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		# Download the page.
		print('Downloading page http://xkcd.com/%s...' % (urlNumber))
		res = requests.get('http://xkcd.com/%s' % (urlnumber))
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text)

		# Find the URL of the comic image.
		comicElem = soup.select('#comic img')
		if comicElem == []:
			print('Could not find comic image.')
		else:
			comicUrl = comicElem[0].get('src')
			# Download the image.
			print('Downloading image %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()

			# Save the image to ./xkcd (the folder)
			imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()

# Create and start the Thread objects.
downloadThreads = []
for i in range(0,1900,100):
	downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
	downloadThreads.append(downloadThread)
	downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
	downloadThread.join()
print('Done.')