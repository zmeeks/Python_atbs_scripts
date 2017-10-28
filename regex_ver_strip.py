#! /usr/bin/env python3
#  regex_ver_strip.py   -- strips whitespace using regex if no argument is given
#					 	-- else strips from string all characters given in passed argument string

"""
README:
Automate The Boring Stuff Python (Ch. 7 -- pg 171) Project
solved by Z Meeks 9/30/17
"""

import re

def rvs(a_string, chars=None):
	if chars == None:
		rvs1(a_string)
	else:
		rvs2(a_string, chars)

def rvs1(a_string):
	stripper = re.compile(r'(\s*)(\S.*\S?)(\s*)')
	found = stripper.search(a_string)
	if found != None:
		print(found.groups()[1])
		return found.groups()[1]
	else:
		print('')
		return ''

def rvs2(a_string, chars):
	chr_str = '[^' + chars + ']'
	stripper = re.compile(chr_str)
	found = stripper.findall(a_string)
	if found != None:
		print(''.join(found))
		return ''.join(found)
	else:
		print('')
		return ''


# function tests :

rvs('   blahbo', 'bl')
rvs('     blah     ')
rvs('     blah blah    ')
rvs('blah blah blah')
