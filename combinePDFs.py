#! /usr/bin/env python3
#  combinePDFs.py -- combines all the PDFs in the current working directory into a single PDF

"""
README:
Automate The Boring Stuff Python (Ch. 13 -- pg 304) Script
copied by Z Meeks 10/03/17
"""

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	# Loop through all the pages (except the first) and add them.
	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()