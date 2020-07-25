#!/usr/bin/env python3

import random
import sys

#read the data file and put it into several data structures

def read_as_string(filename):
	strings = []
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip() #rstrip removes line endings
			strings.append(line)
	return strings


def read_as_list(filename): #a list has square brackets; the difference btwn a tuple and a list is that you cannot modify a tuple
	stuff = []
	with open(filename) as fp:
		for line in fp.readlines():
			f = line.split()
			stuff.append(f)
	return stuff

def read_as_dict(filename):
	pass
	table = {}
	with open(filename) as fp:
		for line in fp.readlines():
			(name, age) = line.split()
			table[name] = int(age) #int(age) allows us to change age into an integer
	return table
	
def read_as_tuple(filename):
	tups = []
	with open(filename) as fp:
		for line in fp.readlines():
			(name, age) = line.split()#tuple is a parenthesis with commas
			#can print(f'{name} is {age} years old'); essentially splits the line into 2 variables
			tups.append((name,int(age))) #to make age a float, just change int(age) to float(age)
	return tups
	
assert(len(sys.argv) == 2) #could also use if len(sys.argv) != 2: print('must include filename') sys.exit()
file = sys.argv[1]

dstr = read_as_string(file)
dlist = read_as_list(file)
ddict = read_as_dict(file)
dtup = read_as_tuple(file)


for (name, age) in dtup:
	print(f'{name} is {age} years old')
	
for a in dlist:
	print(f'{a[0]} is {a[1]} years old') #a[0] gives us the name and a[1] is age
	
for name in ddict:
	print(f'{name} is {ddict[name]} years old')
	
for s in dstr:
	(name, age) = s.split() #splits the string into name and age
	print(f'{name} is {age} years old')
	
#if data is a csv file everything is split by commas
#you would have to do line.split(',') to tell it to split on commas or line.split('/t') to split on tabs
