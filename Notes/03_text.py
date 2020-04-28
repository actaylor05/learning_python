#!/usr/bin/env python3

# Move the triple quotes downward to uncover each segment of code



# Variables with text are called strings

s = 'ACGT' # a string

# Square brackets let you access sub-strings: follow closely below

print(s, s[0], s[1], s[2], s[3]) #you can use -1 to go backwards, -1 will give you a T
print(s[2], s[2:3], s[2:4], s[2:5]) #distance between 2:3 is 1 character and the distance between 2:4 is 2 characters so it will give you 2 letters

# The + operator concatenates strings

s = s + 'N'
s += 'n'   # note that += is a shorthand for s = s +, just like in math
print(s)

# The * operator repeats strings

s *= 3
print(s)

# The len() function returns the length of a string
# Some function like len() return values, others like print() do not

print(len(s))
"""
"""
