#!/usr/bin/env python3

import argparse
import random
import biotools as bt

#File location: ~/Code/learning_python/Week_5/proteins.fasta.gz
# setup
parser = argparse.ArgumentParser(
	description='Predicts trans-membrane proteins.')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='Protein File')

# optional arguments with default parameters
parser.add_argument('--win1', required=False, type=int, default=8,
	metavar='<int>', help='length of signal peptide [%(default)i]')
parser.add_argument('--win2', required=False, type=int, default=11,
	metavar='<int>', help='length of trans-membrane domain [%(default)i]')
parser.add_argument('--kd1', required=False, type=float, default=2.5,
	metavar='<float>', help='kd value for signal peptide [%(default)f]')
parser.add_argument('--kd2', required=False, type=float, default=2.0,
	metavar='<float>', help='kd value for hydrophobic region [%(default)f]')

# finalization
arg = parser.parse_args()



def hh(seq, w, kd):
    for i in range(len(seq) -w +1):
        win = seq[i:i+w]
        if bt.hydro(win) > kd and 'P' not in win:
            return True
    return False
    

for name, seq in bt.read_fasta(arg.file):
    nterm = seq[0:30]
    rest = seq[30:]
    if hh(nterm, arg.win1, arg.kd1) and hh(rest, arg.win2, arg.kd2):
        print(name)