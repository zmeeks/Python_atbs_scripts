#! /usr/bin/env python3
#  removeCsvHeader.py -- removes the header from all CSV files in the current working directory
#  Note on usage:		 Must place program and csv files in same directory

"""
README:
Automate The Boring Stuff Python (Ch. 14 -- pg 325) Script
copied by Z Meeks 10/03/17
"""

import csv, os

os.makedirs('headerRemoved', exist_ok = True)

# Loop through every fjile in the current working directory.
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue 	# skip non-csv files

	print('Removing header from ' + csvFilename + '...')

	# Read in the CSV file, (skipping the first row)
	csvRows = []
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue # skip first row
		csvRows.append(row)
	csvFileObj.close()

	# Write out the CSV file
	csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w') 
	# Note: book had newline = '' in above open() but that caused errors 
	# It isn't supported in Python 3, and by the looks of it it was superflous as was
	(not supported in python 3)
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()
