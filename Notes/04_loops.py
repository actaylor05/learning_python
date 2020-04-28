#!/usr/bin/env python3

import math

# Move the triple quotes downward to uncover each segment of code


# The 'for' loop is one of the most common loop constructs you will use
# Note the indentation of the print(i) statement
# Code 'inside' loops must be indented
# Note that Python starts counting from 0 not 1

for i in range(3):
	print(i)
print('-')
#for loop, range 3 creates a sequence of numbers (0 1 2) 

# The above is really a shortcut for the following code

for i in range(0, 3):
	print(i)
print('--')
#can say explicitly where you want it to start

# But the second construct allows you to set where the loop starts

for i in range(1, 3):
	print(i)
print('---')


# And also the steps between iterations

for i in range(1, 10, 3):
	print(i)
print('----')
# in the first line the first number is where it starts, the second number is where it ends and the last is the step size or how many numbers are skipped

# You can iterate over the characters of a string

s = 'ACGT'
for c in s:
	print(c)
print('-----')

# An alternate way to do the same thing
# It's absolutely critical you understand this code!

for i in range(len(s)):
	print(i, s[i])
print('------')

# Everything that is tabbed-over is within the same loop
# Try removing the tab in front of i += 1 below

i = 0
for c in s:
	print(i, c)
	i += 1
print('-------')
#everything tabbed over is inside the loop, if you take it out of the loop it will no longer work

# The real power begins with loops inside of loops

for i in range(0, 4):
	for j in range(i, 4):
		print(i, j)
print('--------')
#loop inside a loop (0,4) is the whole matrix, (i,4) is half the matrix with the major diagonal (direct comparision)
# by using i+1 it will remove the major diagonal
for i in range(0, 4):
	for j in range(i+1, 4):
		print(i, j)
# Just some fun with loops and math!
"""
precision = 10
e = 0
for n in range(0, precision):
	e += 1/math.factorial(n)
	print(e, math.e - e)

"""
