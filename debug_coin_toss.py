#! /usr/bin/env python3
#  debug_coin_toss.py -- pg. 232

"""
README:
Automate The Boring Stuff Python (Ch.10 -- pg 232) Project
solved by Z Meeks 9/27/17

...Used idle3 debugger...
"""

"""
Original code:

import random
guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads ot tails:')
	guess = input()
toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guesss = input()
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')
"""
# fixed code (fixed in idle3 debugger) = 

import random
guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()
toss = random.choice(['heads', 'tails']) # there was a bug here
if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guess = input() # there was also a bug here
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')
