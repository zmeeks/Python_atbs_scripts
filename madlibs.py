#! /usr/bin/env python3
#  madlibs.py -- A Madlibs generator
#  Usage:	./madlibs.py <sample_file_name.txt> -- reads from sample_file_name.txt and requests user input
#												-- outputs madlib answers to the terminal
#  			./madlibs.py <sample_file_name.txt> <output_file_name.txt> -- input same as single arg (2 sysargs) above
#												-- outputs madlib answers to output_file_name.txt

"""
README:
Automate The Boring Stuff Python (Ch. 8 -- pg 195) Project
solved by Z Meeks 9/26/17

use madlib_samp.txt for an example of how program works
"""

import sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
	print("invalid number of arguments\n")
elif len(sys.argv) == 2:
	text_file = open(sys.argv[1])
	text_str = text_file.read()
	text = text_str.split(' ')
	sz_text = len(text)
	for i in range(0, sz_text):
		if text[i][:9] == 'ADJECTIVE':
			print('Enter an adjective: ')
			text[i] = (input() if len(text[i]) == 9 else input() + text[i][-1])
		elif text[i][:4] == 'NOUN':
			print('Enter a noun: ')
			text[i] = (input() if len(text[i]) == 4 else input() + text[i][-1])
		elif text[i][:4] == 'VERB':
			print('Enter a verb: ')
			text[i] = (input() if len(text[i]) == 4 else input() + text[i][-1])
	for x in text:
		print(x , end=' ')
	print('\n')
elif len(sys.argv) == 3:
	text_file = open(sys.argv[1])
	new_file = open(sys.argv[2], 'w')
	text_str = text_file.read()
	text = text_str.split(' ')
	sz_text = len(text)
	for i in range(0, sz_text):
		if text[i][:9] == 'ADJECTIVE':
			print('Enter an adjective: ')
			text[i] = (input() if len(text[i]) == 9 else input() + text[i][-1])
		elif text[i][:4] == 'NOUN':
			print('Enter a noun: ')
			text[i] = (input() if len(text[i]) == 4 else input() + text[i][-1])
		elif text[i][:4] == 'VERB':
			print('Enter a verb: ')
			text[i] = (input() if len(text[i]) == 4 else input() + text[i][-1])
	for x in text:
		new_file.write(x + ' ')

