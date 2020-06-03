#!/usr/bin/env python3

import fileinput
import random
import json
puncs =  '.,?!:;-*"_()[]{}<>/1234567890—“”’‘–' # you may need to add more
spaces = ' ' * len(puncs)

first = {}
scnd = {}
thrd = {}
for rawline in fileinput.input():

	# convert to lowercase
	lower = rawline.lower()
	
	# convert punctuation to spaces
	table = lower.maketrans(puncs, spaces)
	line = lower.translate(table)
	
	#start work here
	#add an ending character to word
	for word in line.split():
		modword = word + '*'

		#make a dictionary for the first letters (1 letter)
		letter = modword[0]
		if letter in first: first[letter] += 1
		else:				first[letter] = 1
		
		# make a dictionary for remaining letters based on the previous letter: 2nd dimension (2 letters)
		for i in range(1, len(modword)):
			c1 = modword[i-1]
			c2 = modword[i]
			if c1 not in scnd: scnd[c1] = {}
			if c2 not in scnd[c1]: scnd[c1][c2] = 1
			else:                  scnd[c1][c2] += 1
			


		#make a dictionary for remaining letters based on previous: 3rd dimension (3 letters)
		for i in range(2, len(modword)):
			c1 = modword[i-2]
			c2 = modword[i-1]
			c3 = modword[i]
			if c1 not in thrd: thrd[c1] = {}
			if c2 not in thrd[c1]: thrd[c1][c2] = {}
			if c3 not in thrd[c1][c2]: thrd[c1][c2][c3] = 1
			else:                  thrd[c1][c2][c3] += 1
			

#Making a pool to choose the first letter
pool = []
for letter in first:
	for i in range(first[letter]):
		if first[letter] > 1: pool.append(letter)
				
#Making a pool to choose the second letter
pool2 = {}
for c1 in scnd:
	stuff = []
	for c2 in scnd[c1]:
		for i in range(scnd[c1][c2]):
			stuff.append(c2)
	pool2[c1] = stuff

#Making a pool to choose the third letter
pool3 = {}
for c1 in thrd:
	pool3[c1] = {}
	for c2 in thrd[c1]:
		stuff = []
		for c3 in thrd[c1][c2]:
			for i in range(thrd[c1][c2][c3]):
				stuff.append(c3)
		pool3[c1][c2] = stuff
			
#To start choosing the letters
while True:
	word = []
	word.append(random.choice(pool)) #Choose first letter
	word.append(random.choice(pool2[word[0]])) #Choose second letter
	if word[1] == '*': continue
	
	j = 2
	while True: #Choose the third letter
		p2 = word[j-2]
		p1 = word[j-1]
		nxt = random.choice(pool3[p2][p1])
		j += 1
		if nxt == '*': break #* is used to know when to break off a word
		word.append(nxt)
	if 12 > len(word) > 3: #we only want to print words between 3-12 characters (<3 is too short, >12 too long)
		words = ''.join(word)
		print(words.capitalize())
		

"""

"""