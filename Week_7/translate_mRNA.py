#!/usr/bin/env python3

import argparse
import biotools as bt


# Use argparse
# Write a program that translates mRNA
# Assume the protein encoded is the longest ORF
# Use a dictionary for translation and store in biotools

parser = argparse.ArgumentParser(
	description='Translates mRNA.')

parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='FASTA file')

arg = parser.parse_args()


for name, seq in bt.read_fasta(arg.file):
	pro = []
	seq1 = bt.longest_orf(seq)
	for i in range(0, len(seq1), 3):
		codon = seq1[i:i+3]
		if codon in bt.aa: pro.append(bt.aa[codon])
		else:              pro.append('X') # how to deal with Ns and such
	print(f'>{name}')
	print(''.join(pro))



"""
python3 translate_mRNA.py --file transcripts.fasta.gz
>CBG00001.1
MTFCENKNLPKPPSDRCQVVVISILSMILDFYLKYNPDKHWAHLFYGASPILEILVIFGMLANSVYGNKLAMFACVLDLVSGVFCLLTLPVISVAENATGVRLHLPYISTFHSQFSFQVSTPVDLFYVATFLGFVSTILILLFLILDALKFMKLRKLRNEDLEKEKKMNPIEKV*
>CBG00006.1
MNGVEKVNKYFDIKDKRDFLYHFGFGVDTLDIKAVFGDTKFVCTGGSPGRFKLYAEWFAKETSIPCSENLSRSDRFVIYKTGPVCWINHGMGTPSLSIMLVESFKLMHHAGVKNPTFIRLGTSGGVGVPPGTVVVSTGAMNAELGDTYVQVIAGKRIERPTQLDATLREALCAVGKEKNIPVETGKTMCADDFYEGQMRLDGYFCDYEEEDKYAFLRKLNSLGVRNIEMESTCFASFTCRAGFPSAIVCVTLLNRMDGDQVQIDKEKYIEYEERPFRLVTAYIRQQTGV*
etc.
"""
