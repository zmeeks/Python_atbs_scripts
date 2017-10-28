#! /usr/bin/env python3
#  randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key

"""
README:
Automate The Boring Stuff Python (Ch. 8 -- pg 186) Script/Project
solved by Z Meeks 9/26/17

note: this script sounded fun and so I solved it before looking at answer
-- see other folder for book's solution -- my solution distributes wrong answers better
"""

import random

# quiz data : keys are states, values are states' capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',  
'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 
'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 
'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 
'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 
'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 
'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}

states = list(capitals.keys())
master_list = [] 	# to ensure that the randomized questions containt the same random wrong answers
ans_key = []		# to keep track of the correct answer
shuffler = list(range(0,50))  #to ensure with high probability different orderings of the questions

#populate master_list 
for i in range(0,50):
	a_list = [states[i]]
	while len(a_list) < 4:
		rand_state = random.choice(states)
		if rand_state not in a_list:
			a_list.append(rand_state)
	master_list.append(a_list)

#populate ans_key
for i in range(0,50):
	ans_key.append(master_list[i][0])

#shuffle everything for the 35 quizzes and populate those quizes and write the quiz and answer keys to this folder
for quizNum in range(1,36):
	quiz_str = 'quiz_' + str(quizNum) + '.txt'
	ans_str = 'ansKey_' + str(quizNum) + '.txt'
	random.shuffle(shuffler)
	quiz_file = open(quiz_str, 'w')
	ans_file = open(ans_str, 'w')
	quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quiz_file.write(' '*20 + 'U.S. Capitals Quiz -- Version ' + str(quizNum) + '\n\n')
	ans_file.write(' '*20 + 'U.S. Capitals Answer Key -- Version ' + str(quizNum) + '\n\n')
	for ind, item in enumerate(shuffler):
		random.shuffle(master_list[item])
		quiz_file.write('#'+str(ind+1)+': What is the capital of '+ans_key[item]+'? :\n')
		ans_file.write('#'+str(ind+1)+'= '+'ABCD'[master_list[item].index(ans_key[item])]+'\n')
		for i,x in enumerate(master_list[item]):
			quiz_file.write(' '*5 + 'ABCD'[i] + '. ' + capitals[x] + '\n')
		quiz_file.write('\n')
	quiz_file.close()
	ans_file.close()
