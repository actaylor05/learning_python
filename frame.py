#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

s = 'ATGGCCTTT'
x = 0
print('Nested Loop:')
for i in range (0, len(s), 3):
    for j in range (0,3):
        print (x, j, s[x])
        x += 1
print ('---------') 
print('Single Loop:')      
x=0        
for i in range (0, len(s), 3):
    print (x,0,s[x])
    x += 1
    print (x,1, s[x])
    x += 1
    print (x,2, s[x])
    x += 1
    
"""
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
