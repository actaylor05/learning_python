#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Step size is 5 nt
# Output with 4 significant figures using whichever method you prefer
# Use nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
s = 5
gc_count = 0
for i in range(0, len(seq) -w+1, s):
    kmer = seq[i:i+w]
    for j in range(0,w):
        if kmer[j] == 'C' or kmer[j] == 'G':
            gc_count += 1
    print(i, kmer, '%.4f' % (gc_count / w))
    gc_count = 0
print('------')

#Korf's Version
for i in range (len(seq) -w +1, s): #you need -w +1 because -w will make you miss one line
    sseq = seq[i:i+w]
    gc = 0
    for nt in sseq:
        if nt == 'G' or nt == 'C':
            gc += 1
    print(i, sseq, gc/w)

"""
0 ACGACGCAGGA 0.6364
5 GCAGGAGGAGA 0.6364
10 AGGAGAGTTTC 0.4545
15 AGTTTCAGAGA 0.3636
20 CAGAGATCACG 0.5455
25 ATCACGAATAC 0.3636
30 GAATACATCCA 0.3636
35 CATCCATATTA 0.2727
40 ATATTACCCAG 0.3636
45 ACCCAGAGAGA 0.5455
"""
