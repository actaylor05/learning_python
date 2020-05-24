#!/usr/bin/env python3

# Write a program that computes hydrophobicity in a window
# Let the user choose the method (see below)
# https://en.wikipedia.org/wiki/Hydrophilicity_plot
# https://en.wikipedia.org/wiki/Hydrophobicity_scales

#dictionaries and function is stored in biotools
import argparse
import biotools as bt

parser = argparse.ArgumentParser(
	description='Hydrophobicity Calculator.')

parser.add_argument('--input', required=True, type=str,
	metavar='<str>', help='File input')
parser.add_argument('--method', required=True, type=str, default='KD',
	metavar='<str>', help='Method used to calculate Hydrophobicity: KD, IS, OS, IS+OS')
parser.add_argument('--window', required=False, type=int, default=11,
	metavar='<int>', help='Window Size[%(default)i]')

arg = parser.parse_args()


for name, seq in bt.read_fasta(arg.input):
	for i in range(len(seq) - arg.window +1):
		win = seq[i:i + arg.window]
		print(bt.cal_hydrophobicity(win, arg.method, arg.window))

"""
	for i in range(len(seq)):
		win = seq[i:i+w]
python3 hydrophobicity.py --input proteins.fasta.gz --window 11 --method kd
"""
