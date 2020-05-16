#!/usr/bin/env python3

import gzip
import sys
import biotools as bt
import argparse

# Use argparse
# Write a program that translates an mRNA
# Assume the protein encoded is the longest ORF
#../Week_5/transcripts.fasta.gz

parser = argparse.ArgumentParser(
	description='Translates mRNA.')

parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='FASTA file')

arg = parser.parse_args()


for name, seq in bt.read_fasta(arg.file):
		print(f'>{name}')
		print(bt.longest_orf(seq))
		


