#!/usr/bin/env python3

#GC

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

count = 0
for nt in dna:
    if nt == 'G' or nt == 'C': count += 1
fraction = count / len(dna)

print(f'{fraction:.2f}')

print('----------')

#GC win

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11

for i in range(0, len(seq)-w +1, 1):
    win = seq[i:i+w]
    gc = 0
    for nt in seq:
        if nt == 'G' or nt == 'C': gc += 1
    gc_frac = gc/w 
    print(i, win, gc)
    
#GC win using a function
seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11

def gc(seq):
    gc = 0
    for nt in seq:
        if nt == 'G' or nt == 'C': gc += 1
    return gc / len(seq)
    
for i in range(len(seq)-w +1):
    print(i, seq[i:i+w], gc(seq[i:i+w]))
    
#Stats
from math import sqrt
import fileinput

data = []

for line in fileinput.input():
    if line.startswith('#'): continue
    line = line.rstrip()
    data.append(float(line))
    
data.sort
count = len(data)
min = data[0]
max = data[-1]

sum = 0
for d in data:
    sum += d
mean = sum/count

#PepSearch
import gzip
import sys

def read_fasta(filename):
    Name = None
    seqs = []
    
    fp = None
    if filename == '-':
        fp = sys.stdin
    elif filename.endswith('.gz'):
        fp = gzip.open(filename, 'rt')
    else:
        fp = open(filename)

    for line in fp.readlines():
        line = line.rstrip()
        if line.startswith('>'):
            if len(seqs) > 0:
                seq = ''.join(seqs)
                yield(name, seq)
                name = line[1:]
                seqs = []
            else:
                name = line[1:]
        else:
            seqs.append(line)
    yield(name, ''.join(seqs))
    fp.close()


filename = sys.argv[1]
pat = sys.argv[2]
for name, seq in read_fasta(sys.argv[1]):
    if pat in seq: print(name, len(seq))
    
#pepSearch longest/shortest pep
import gzip
import sys
import math

def read_fasta(filename):
    Name = None
    seqs = []
    
    fp = None
    if filename == '-':
        fp = sys.stdin
    elif filename.endswith('.gz'):
        fp = gzip.open(filename, 'rt')
    else:
        fp = open(filename)

    for line in fp.readlines():
        line = line.rstrip()
        if line.startswith('>'):
            if len(seqs) > 0:
                seq = ''.join(seqs)
                yield(name, seq)
                name = line[1:]
                seqs = []
            else:
                name = line[1:]
        else:
            seqs.append(line)
    yield(name, ''.join(seqs))
    fp.close()


filename = sys.argv[1]
longest = -1
shortest = math.inf
for name, seq in read_fasta(sys.argv[1]):
    if len(seq) > longest: longest = len(seq)
    if len(seq) < shortest: shortest = len(seq)
print(shortest, longest)