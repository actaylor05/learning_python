#!/usr/bin/env python3

import fileinput
import random
import json
puncs =  '.,?!:;-*"_()[]{}<>/1234567890—“”’‘–' # you may need to add more
spaces = ' ' * len(puncs)

first = {}
scnd = {}
for rawline in fileinput.input():

	# convert to lowercase
	lower = rawline.lower()
	
	# convert punctuation to spaces
	table = lower.maketrans(puncs, spaces)
	line = lower.translate(table)
	
	# start work here
	#add an ending character to word
	for word in line.split():
		modword = word + '*'
		
		#make a dictionary for the first letters
		letter = modword[0]
		if letter in first: first[letter] += 1
		else:				first[letter] = 1
		
		# make a dictionary for all remaining letters based on the previous letter
		for i in range(1, len(modword)):
			c1 = modword[i-1]
			c2 = modword[i]
			if c1 not in scnd: scnd[c1] = {}
			if c2 not in scnd[c1]: scnd[c1][c2] = 1
			else:                  scnd[c1][c2] += 1
		
		
#print(json.dumps(scnd, indent=4))
		

#the way to choose the first letter
pool = []
for letter in first:
	for i in range(first[letter]):
		if first[letter] > 1: pool.append(letter)
				
pool2 = {}
for c1 in scnd:
	stuff = []
	for c2 in scnd[c1]:
		for i in range(scnd[c1][c2]):
			stuff.append(c2)
	pool2[c1] = stuff
#print(pool)
#print(pool2)

for i in range(30):
	word = []
	word.append(random.choice(pool))
	for j in range(1, 15):
		prv = word[j-1]
		nxt = random.choice(pool2[prv])
		if nxt == '*': break
		word.append(nxt)
	if len(word) > 1:
		print(''.join(word))

#based on what r is, reference scnd dictionary 
		#choose random letter from [let_2] based on what was chosen(r/[let_1])
		#append the 2nd letter to first letter(r)
	#fill in letters until a * is chosen
		#when * is hit break the word
	#OR randomly add strings of letters between lengths 0 to 7 to each two letter word that is created
	#print each created word
"""

#make a random number generator that choses some letter more frequently over others
#make the 2nd dictionary depend on the second letter, make the 3rd dictionary choose from any number of letters and the ending symbol
		
		

"""