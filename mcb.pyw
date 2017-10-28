#! /usr/bin/env python3
#  mcb.pyw -- saves and loads pieces of text to the clipboard
#  Usage:	./mcb.pyw save <keyword> -- saves clipboard to keyword
#			./mcb.pyw <keyword> -- Loads keyword to clipboard
#			./mcb.pyw list -- Loads all keywords to clipboard
#  Note:	do not use 'list' as a keyword

"""
README:
Automate The Boring Stuff Python (Ch. 8 -- pg 192) Script
copied by Z Meeks 9/26/17
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1] == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()