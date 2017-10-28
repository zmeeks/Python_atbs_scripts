#! /usr/bin/env python3
#  pword_strength_chk.py -- password strength checker -- detects whether a potential password is strong enough
#  Usage:		./pword_strength_chk.py <password>

"""
README:
Automate The Boring Stuff Python (Ch. 7 -- pg 171) Project
solved by Z Meeks 9/30/17

This script checks whether or not a password is strong enough given the following constraints:
-password is at least 8 chars long
-contains both lowercase and uppercase chars
-contains at least one number
-must be solved using regular expressions
"""

import re, sys

if len(sys.argv) != 2:
	print("Incorrect number of arguments given")
	sys.exit()
pword = sys.argv[1]
pwc1 = re.compile(r'\S{8,}')
pwc2 = re.compile(r'[a-z]')
pwc3 = re.compile(r'[A-Z]')
pwc4 = re.compile(r'[0-9]')
if pwc1.search(pword) == None:
	print('Password not strong enough')
elif pwc2.search(pword) == None:
	print('Password not strong enough')
elif pwc3.search(pword) == None:
	print('Password not strong enough')
elif pwc4.search(pword) == None:
	print('Password not strong enough')
else:
	print('Password is strong enough :)')