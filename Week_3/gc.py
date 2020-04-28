#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods
print('Method 1: printf()')
seq = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gc_count = 0
for i in range(0, len(seq)):
    if seq[i] == 'G' or seq[i] == 'C':
        gc_count += 1
print ('%.2f' % (gc_count / len(seq)))

print('-----')

print('Method 2: str.format()')
gc_count = 0
for i in range(0, len(seq)):
    if seq[i] == 'G' or seq[i] == 'C':
        gc_count += 1
print ('{:.2f}'.format (gc_count / len(seq)))

print('------')

print('Method 3: f-strings')
gc_count = 0
for i in range(0, len(seq)):
    if seq[i] == 'G' or seq[i] == 'C':
        gc_count += 1
print (f'{gc_count / len(seq):.2f}')

print('------')

print('Korfs method')
gc_count = 0
for c in seq:
    if c == 'G' or c == 'C':
        gc_count += 1
print(f'{gc_count / len(seq):.2f}')


'''
0.42
0.42
0.42
'''