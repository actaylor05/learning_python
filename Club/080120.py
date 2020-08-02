#!/usr/bin/env python3

#A program that will take a sequence in IUPAC and make it in As Cs Gs and Ts

import json
import sys

iupac = {
		'A':['A'],
		'C':['C'],
		'G':['G'],
		'T':['T'],
		'R':['A', 'G'],
		'Y':['C', 'T'],
		'S':['C', 'G'],
		'W':['A', 'T'],
		'M':['A', 'C'],
		'K':['G', 'T'],
		'B':['C', 'G', 'T'],
		'D':['A', 'G', 'T'],
		'H':['A', 'C', 'T'],
		'V':['A', 'C', 'G'],
		'N':['A', 'C', 'G', 'T']
}

dna = sys.argv[1]

for nt in dna:
	if len(iupac[nt]) == 1:
		print(nt, end='-')
	else:
		print(f'[{"".join(iupac[nt])}]', end="-")
		
print() #No clue what this statement does, but code does not work w/o it


print('------------')

#Markov Model using dictionaries

states = ['S1', 'S2', 'S3']

markov = {
		'S1': {'S1': 0.8, 'S2':0.1, 'S3':0.1},
		'S2': {'S1': 0.3, 'S2':0.4, 'S3': 0.3},
		'S3': {'S1':0.1, 'S2': 0.2, 'S2': 0.7}
}

print(json.dumps(markov, indent=4))

#Markov Model using tuples

states = ('Exon', 'Intron', 'Genomic')

mt = (
		(0.8, 0.1, 0.1),
		(0.3, 0.4, 0.3),
		(0.1, 0.2, 0.7)
)

print(json.dmps(mt, indent=4))

#for a HMM you need emission probs
#ep = {
#		'Exon':{'A':0.25, 'C': 0.25 .......}
#}