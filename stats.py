#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

data = []
total = 0
count = 0
for line in fileinput.input():
    if line.startswith('#'): continue
    line = line.rstrip()
    total += float(line)
    data.append(float(line))
count = int(len(data))    
mean = total/len(data)
stddev = 0

for i in range(0, len(data)):
    stddev += (data[i] - mean) * (data[i] - mean)
stddev = sqrt(stddev/(count))

data.sort()
min = data[0]
max = data[-1]

if count % 2 == 0:
    median1 = data[int(count/2)-1]
    median2 = data[int(count/2)]
    median = (median1 + median2)/2
else:
    median = data[int(count/2)-1]
    

print(f'Count: {count}')
print(f'Minimum: {min}')
print(f'Maximum: {max}')
print(f'Mean: {mean}')
print('Std. dev: ''%.3f' % (stddev))
print(f'Median: {median}')




"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
