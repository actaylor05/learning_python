#!/usr/bin/env python3


# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

#Frame

dna = 'ATGGCCTTT'
for i in range(0, len(dna)):
    print(i, i%3, dna[i])
    
print('-------')
    
#Do this showing all possible frames
dna = 'ATGGCCTTT'

for frame in range(3):
    print(f'Frame:{frame}')
    for i in range(0, len(dna) -2 -frame, 3):
        print(i, dna[i + frame: i + 3+frame])

# Print out all the kmers for a given size

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

k = 3
for i in range(0, len(dna) -k+1):
    print(dna[i: i+k])

print('-------')

#write a function that calculates the factorial of a number
def fac(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

for i in range(1, 5):
    print(i, float(fac(i)))
    
#AA pairs
aa = 'ACDEFGHIKLMNPQRSTVWY'

for i in range(0, len(aa)):
    for j in range(i + 1, len(aa)):
     print(aa[i], aa[j])
     
print('--------')

#at_seq
import random
#if you put random.seed here you will have the same seed in the entire program
def at_seq(length, at):
    dna = ''
    for i in range(length):
        r = random.random()
        if r < at:
            r = random.random()
            if r < 0.5: dna += 'A'
            else:       dna += 'T'
        else:
            r = random.random()
            if r < 0.5: dna += 'G'
            else:       dna += 'C'
    return dna
    
for i in range(3):
    #if you put random.seed here you will have a different seed for each iteration of the loop
    print(at_seq(30, 0.6))

print('---------')

#fizzbuzz
#print fizz for multiple of 3, print buzz for multiples of 5, and fizzbuzz for multiples of 3 and 5
for i in range(1, 101):
    if i%3 == 0 and i%5 == 0: print('fizzbuzz')
    elif i%3 == 0: print('fizz')
    elif i%5 == 0: print('buzz')
    else:          print(i)















