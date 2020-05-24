#!/usr/bin/env python3

#count all kmers in a DNA sequence
#Loop through the sequences(multiple seqs per file); create kmers; display kmers
import biotools as bt
import sys

total_ct = {}
k = 2
for name, seq in bt.read_fasta(sys.argv[1]):
	kmers_ct = {}
	for i in range(len(seq)-k +1):
		kmer = seq[i:i+k]
		if kmer in kmers_ct: kmers_ct[kmer] += 1
		else:				 kmers_ct[kmer] = 1
		if kmer in total_ct: total_ct[kmer] += 1
		else:				 total_ct[kmer] = 1
	print(kmers_ct)
print('--------')
print(total_ct)


#if you want to print each chromosome, kmers_ct dictionary needs to be inside the loop
#if you want for the entire genome, kmers_ct dictionary needs to be outside the loop
