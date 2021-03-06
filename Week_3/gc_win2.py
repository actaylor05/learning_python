#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops
# Describe the pros/cons of this algorith vs. nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11

for i in range(0, len(seq) -w+1):
    kmer = seq[i:i+w]
    gc_count = 0
    if kmer[0] == 'C' or kmer[0] == 'G':
        gc_count += 1
    if kmer[1] == 'C' or kmer[1] == 'G':
        gc_count += 1
    if kmer[2] == 'C' or kmer[2] == 'G':
        gc_count += 1
    if kmer[3] == 'C' or kmer[3] == 'G':
        gc_count += 1
    if kmer[4] == 'C' or kmer[4] == 'G':
        gc_count += 1
    if kmer[5] == 'C' or kmer[5] == 'G':
        gc_count += 1
    if kmer[6] == 'C' or kmer[6] == 'G':
        gc_count += 1
    if kmer[7] == 'C' or kmer[7] == 'G':
        gc_count += 1
    if kmer[8] == 'C' or kmer[8] == 'G':
        gc_count += 1
    if kmer[9] == 'C' or kmer[9] == 'G':
        gc_count += 1
    if kmer[10] == 'C' or kmer[10] == 'G':
        gc_count += 1
    print(i, kmer, '%.4f' % (gc_count / w))
    
print('--------')

#Another way to do this with string functions (I don't think we have learned this yet)

for i in range(0, len(seq) -w+1):
    kmer = seq[i:i+w]
    gc_count = 0
    gc_count += kmer.count('G')
    gc_count += kmer.count('C')
    print(i, kmer, '%.4f' % (gc_count / w))
    
print('------')
#Korf's Version

gc = 0
for i in range (0,w):
    if seq[i] == 'G' or seq[i] == 'C':
        gc += 1
print(0, seq[0:w], gc/w)

for i in range(1, len(seq) -w +1):
    prev = seq[i-1]
    nex = seq[i+w-1]
    if prev == 'G' or prev == 'C':
        gc -= 1
    if nex == 'G' or nex == 'C':
        gc += 1
    print(i, seq[i:i+w], gc/w)

    
#Pros: Some pros to using single loops would be that it may be more intuitive than the nested loops. Single loops may initially be more logical because you would not 
#necessarily have to consider how many iterations you would need to have to complete what you need done. Another pro may be that with single loops, the coding could 
#be less complex as you would not have to consider using multiple loops and making sure they are nestled properly and run the proper amount of times. 

#Cons: One con could be that if you were to do a single loop it may end up making the code longer than it needed to be with nested loops. Another con could
#be that depending on the coding for the single loop, it would not be nearly as flexible as the nested loop (the first single loop code I did is not flexible to changes whereas
#the second one with string functions is). In the nested loop it was easier to incorporate flexibility into the code so that you could easily change the window size 
#or sequence length.

"""
0 ACGACGCAGGA 0.6364
1 CGACGCAGGAG 0.7273
2 GACGCAGGAGG 0.7273
3 ACGCAGGAGGA 0.6364
4 CGCAGGAGGAG 0.7273
5 GCAGGAGGAGA 0.6364
6 CAGGAGGAGAG 0.6364
7 AGGAGGAGAGT 0.5455
8 GGAGGAGAGTT 0.5455
9 GAGGAGAGTTT 0.4545
10 AGGAGAGTTTC 0.4545
11 GGAGAGTTTCA 0.4545
12 GAGAGTTTCAG 0.4545
13 AGAGTTTCAGA 0.3636
14 GAGTTTCAGAG 0.4545
15 AGTTTCAGAGA 0.3636
16 GTTTCAGAGAT 0.3636
17 TTTCAGAGATC 0.3636
18 TTCAGAGATCA 0.3636
19 TCAGAGATCAC 0.4545
20 CAGAGATCACG 0.5455
21 AGAGATCACGA 0.4545
22 GAGATCACGAA 0.4545
23 AGATCACGAAT 0.3636
24 GATCACGAATA 0.3636
25 ATCACGAATAC 0.3636
26 TCACGAATACA 0.3636
27 CACGAATACAT 0.3636
28 ACGAATACATC 0.3636
29 CGAATACATCC 0.4545
30 GAATACATCCA 0.3636
31 AATACATCCAT 0.2727
32 ATACATCCATA 0.2727
33 TACATCCATAT 0.2727
34 ACATCCATATT 0.2727
35 CATCCATATTA 0.2727
36 ATCCATATTAC 0.2727
37 TCCATATTACC 0.3636
38 CCATATTACCC 0.4545
39 CATATTACCCA 0.3636
40 ATATTACCCAG 0.3636
41 TATTACCCAGA 0.3636
42 ATTACCCAGAG 0.4545
43 TTACCCAGAGA 0.4545
44 TACCCAGAGAG 0.5455
45 ACCCAGAGAGA 0.5455
46 CCCAGAGAGAG 0.6364
"""
