#!/usr/bin/env python3

import gzip
import sys

# We have imported modules like math, sys, and gzip a few times
# You can also write and import your own modules

import biotools as bt

#from biotools import read_fasta allows you to import a specific function within biotools

# The read_fasta() and gc() functions are in biotools.py (take a look)

for name, seq in bt.read_fasta('genome.fa.gz'):
	print(name, len(seq))
	
#soft link: ln -s biotools.py . allows us to point to where the directory is


