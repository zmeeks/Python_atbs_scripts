#! /usr/bin/env python3
#  mcb.pyw -- saves and loads pieces of text to the clipboard
#  Usage:	./mcb.pyw save <keyword> -- saves clipboard to keyword
#			./mcb.pyw <keyword> -- Loads keyword to clipboard
#			./mcb.pyw list -- Loads all keywords to clipboard
#  Note:	do not use 'list' as a keyword

"""
README:
Automate The Boring Stuff Python (Ch. 8 -- pg 194) Project
solved by Z Meeks 9/26/17
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcbx')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1] == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1] == 'delete':
	del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
	# Lists keywords
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	# deletes all keywords
	elif sys.argv[1].lower() == 'delete':
		for x in mcbShelf:
			del mcbShelf[x]
	#loads content
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()