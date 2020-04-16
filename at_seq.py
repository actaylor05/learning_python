#!/usr/bin/env python3

import random
'''random.seed(1)''' # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence
'''
length =30
dna = ''
for i in range(length):
	r = random.randint(1, 4) # generate a random number from 1 to 4
	if   r == 1: dna += 'A'
	elif r == 2: dna += 'C'
	elif r == 3: dna += 'G'
	else:        dna += 'T'
print(dna)

length =30
dna = ''
alph = 'ACGT'
for i in range(length):
	r = random.randint(1, 4) # generate a random number from 1 to 4
	if   r == 1: dna += 'A'
	elif r == 2: dna += 'C'
	elif r == 3: dna += 'G'
	else:        dna += 'T'
print(dna)
'''
length =30
dna = ''
at_count = 0
for i in range(length):
    r = random.random ()
    if r < 0.6:
        r = random.randint(0,1)
        if r == 0: dna += 'A'
        else:      dna += 'T'
        at_count += 1
    else:
        r = random.randint(0,1)
        if r == 0: dna += 'C'
        else:      dna += 'G'
print(length, at_count / length, dna)

print('-------')

length =30
dna = ''
at_count = 0
alphabet = 'AAAAAAAAAAAAAAAAAAAACGCGTTT'
for i in range(length):
    nt = random.choice (alphabet)
    if nt == 'A' or nt == 'T': at_count += 1
    dna += nt
print(length, at_count / length, dna)
"""
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
