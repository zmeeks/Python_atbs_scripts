#! /usr/bin/env python3
# printTable.py - solution to printTable practice project

"""
README:
Automate The Boring Stuff Python (Ch. 6pg 143) Project
solved by Z Meeks 9/19/17

note: tableData is the test list given in the problem statement
"""

def printTable(listOfStrs):
	colWidths = [0]*len(listOfStrs)
	for i in range(0, len(listOfStrs)):
		maxi = 0
		for x in listOfStrs[i]:
			maxi = max(maxi, len(x))
		colWidths[i] = maxi

	for j in range(0, len(listOfStrs[0])):
		for i in range(0, len(listOfStrs)):
			print(listOfStrs[i][j].rjust(colWidths[i]), end = ' ')
		print() # add a new line

tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)  # test the function