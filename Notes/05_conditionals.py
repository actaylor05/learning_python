#!/usr/bin/env python3

import random

# Move the triple quotes downward to uncover each segment of code



# The standard conditional statement is a single 'if'
"""
a = 1
b = 2

if a < b:
	print('Yes, a < b')

# We can assign the expression (a < b) to a variable

c = a < b
print(c)
print(type(c))

# Variables of type 'bool' can be True or False
# Often we want to ask about multiple exclusive conditions
# In the example below, we use the randint() function from the random module

r = random.randint(1, 4) # generate a random number from 1 to 4
if   r == 1: print('A')
elif r == 2: print('C')
elif r == 3: print('G')
else:        print('T')

# Let's put that code above into a loop and generate some random sequence
# Note the use of end='' to prevent starting a new line
#random.seed(#) will give us the same random sequence output each time
length = 10
for i in range(length):
	r = random.randint(1, 4) # generate a random number from 1 to 4
	if   r == 1: print('A', end='')
	elif r == 2: print('C', end='')
	elif r == 3: print('G', end='')
	else:        print('T', end='')
print()
#to abort a method hit control C, control Z will send a sleep command
#end= means not to put any character at the end, usually it creates a return but now we want our letters to look like sequence
#can use end. to print a . after each letter
"""
# The Boolean operators are 'and', 'or', and 'not'

# Print out all the positions that are A or T
# Note the use of 'or'

dna = 'ACGTGGGGT'
for i in range(len(dna)):
	nt = dna[i]
	if nt == 'A' or nt == 'T':
		print('W at', i) # W is IUPAC for A or T

# Let's print all the positions with a CG di-nucleotide
# Note the use of 'and'
# Why is there a -1 in the code below?

for i in range(len(dna) -1): #we use the -1 to prevent it from going off of the string
	if dna[i] == 'C' and dna[i+1] == 'G':
		print('CG at', i)

# Print out all letters that are not G
# Note the switch from range() to iterating letters in sequence

for nt in dna:
	if not nt == 'G':
		print(nt)

# The 'while' loop mixes a conditional with a loop

i = 0
while (False):          # change False to True and back, when you change it to True it will run forever
	print('forever', i) # hit ^C to break the loop
	i += 1
    # can us if i == 50 break (will break the loop when i equals 50
# you can change the while(#) to give it a condition ex while(i<100) the loop will continue to run until i is over 100
"""
"""