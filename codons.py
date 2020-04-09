#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(codon)

print('-----------')

#Another way to write the code would be
for i in range(0, len(dna), 3):
    print(dna[i:i+3])

print('---------')

#Using different frames
print('Varying Reading Frames:')
for f in range(3):
    print('frame', f)
    for i in range(f, len(dna) -2, 3):
        codon = dna[i:i+3]
        print(codon)   
        
print('--------')        
#kmers; you can change k to any number to get different lengths of kmers
print('kmers:')
k=4 
for i in range(0, len(dna) -k+1):
    kmer = dna[i:i+4]
    print(kmer)         
    


"""
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
