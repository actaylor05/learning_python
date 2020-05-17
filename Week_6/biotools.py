#!/usr/bin/env python3

import sys
import gzip
import random

def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

def gc(seq):
	count = 0
	for nt in seq:
		if nt == 'G' or nt == 'C':
			count += 1
	return count / len(seq)
	
def randseq(l, gc):
	dna = []
	for i in range(l):
		r = random.random()
		if r < gc:
			r = random.random()
			if r < 0.5: dna.append('G')
			else:		dna.append('C')
		else:
			r = random.random()
			if r < 0.5: dna.append('A')
			else:		dna.append('T')
	return ''.join(dna)
	
def hydro(seq):
	kd = 0
	for aa in seq:
		if aa == 'I': kd += 4.5
		elif aa == 'V': kd += 4.2
		elif aa == 'L': kd += 3.8
		elif aa == 'F': kd += 2.8
		elif aa == 'C': kd += 2.5
		elif aa == 'M': kd += 1.9
		elif aa == 'A': kd += 1.8
		elif aa == 'G': kd += -0.4
		elif aa == 'T': kd += -0.7
		elif aa == 'S': kd += -0.8
		elif aa == 'W': kd += -0.9
		elif aa == 'Y': kd += -1.3
		elif aa == 'P': kd += -1.6
		elif aa == 'H': kd += -3.2
		elif aa == 'E': kd += -3.5
		elif aa == 'Q': kd += -3.5
		elif aa == 'D': kd += -3.5
		elif aa == 'N': kd += -3.5
		elif aa == 'K': kd += -3.9
		elif aa == 'R': kd += -4.5
	return kd / len(seq)
	
def skew(seq): #(g-c)/(g+c)
	g_count = 0
	c_count = 0
	for nt in seq:
		if nt == 'G': g_count += 1
		elif nt == 'C': c_count += 1
	return (g_count - c_count) / (g_count + c_count)
	
def longest_orf(seq):
	atgs = []
	for i in range(len(seq) -2):
		if seq[i:i+3] == 'ATG': atgs.append(i)
	max_len = 0
	max_seq = None
	for atg in atgs:
		stop = None
		for i in range(atg, len(seq) -2, 3):
			codon = seq[i:i+3]
			if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
				stop = i 
				break
		if stop != None:
			cds_len = stop - atg +3
			if cds_len > max_len:
				max_len = cds_len
				max_seq = seq[atg:atg+cds_len]
	return translate(max_seq)
	if max_seq == None: return None
	
def translate(seq):
	assert(len(seq) % 3 == 0)
	pro = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon == 'AAA': pro.append('K')
		elif codon == 'AAC': pro.append('N')
		elif codon == 'AAT': pro.append('N')
		elif codon == 'AAG': pro.append('K')
		elif codon == 'ACA': pro.append('T')
		elif codon == 'ACC': pro.append('T')
		elif codon == 'ACT': pro.append('T')
		elif codon == 'ACG': pro.append('T')
		elif codon == 'AGA': pro.append('R')
		elif codon == 'AGC': pro.append('S')
		elif codon == 'AGT': pro.append('S')
		elif codon == 'AGG': pro.append('R')
		elif codon == 'ATA': pro.append('I')
		elif codon == 'ATC': pro.append('I')
		elif codon == 'ATT': pro.append('I')
		elif codon == 'ATG': pro.append('M')

		elif codon == 'CAC': pro.append('H')
		elif codon == 'CAT': pro.append('H')
		elif codon == 'CAG': pro.append('Q')
		elif codon == 'CAA': pro.append('Q')
		elif codon == 'CCA': pro.append('P')
		elif codon == 'CCC': pro.append('P')
		elif codon == 'CCT': pro.append('P')
		elif codon == 'CCG': pro.append('P')
		elif codon == 'CGA': pro.append('R')
		elif codon == 'CGC': pro.append('R')
		elif codon == 'CGT': pro.append('R')
		elif codon == 'CGG': pro.append('R')
		elif codon == 'CTA': pro.append('L')
		elif codon == 'CTC': pro.append('L')
		elif codon == 'CTT': pro.append('L')
		elif codon == 'CTG': pro.append('L')

		elif codon == 'GAC': pro.append('D')
		elif codon == 'GAA': pro.append('E')
		elif codon == 'GAT': pro.append('D')
		elif codon == 'GAG': pro.append('E')
		elif codon == 'GCA': pro.append('A')
		elif codon == 'GCC': pro.append('A')
		elif codon == 'GCT': pro.append('A')
		elif codon == 'GCG': pro.append('A')
		elif codon == 'GGA': pro.append('G')
		elif codon == 'GGC': pro.append('G')
		elif codon == 'GGT': pro.append('G')
		elif codon == 'GGG': pro.append('G')
		elif codon == 'GTA': pro.append('V')
		elif codon == 'GTC': pro.append('V')
		elif codon == 'GTT': pro.append('V')
		elif codon == 'GTG': pro.append('V')
		
		elif codon == 'TAC': pro.append('Y')
		elif codon == 'TAA': pro.append('X')
		elif codon == 'TAT': pro.append('Y')
		elif codon == 'TAG': pro.append('X')
		elif codon == 'TCA': pro.append('S')
		elif codon == 'TCC': pro.append('S')
		elif codon == 'TCT': pro.append('S')
		elif codon == 'TCG': pro.append('S')
		elif codon == 'TGA': pro.append('X')
		elif codon == 'TGC': pro.append('C')
		elif codon == 'TGT': pro.append('C')
		elif codon == 'TGG': pro.append('W')
		elif codon == 'TTA': pro.append('L')
		elif codon == 'TTC': pro.append('F')
		elif codon == 'TTT': pro.append('F')
		elif codon == 'TTG': pro.append('L')
		
		else: pro.append(X)
	return ''.join(pro)

def entropy(seq, w):
	for i in range(len(seq) -w +1):
		win = seq[i: i+ w]
		a_ct = 0.00001
		c_ct = 0.00001
		g_ct = 0.00001
		t_ct = 0.00001
		for nt in win:
			p = []
			if nt == 'A': a_ct += 1
			elif nt == 'C': c_ct += 1
			elif nt == 'G': g_ct += 1
			elif nt == 'T': t_ct += 1
			aprob = float(a_ct/w)
			p.append(aprob)
			cprob = float(c_ct/w)
			p.append(cprob)
			gprob = float(g_ct/w)
			p.append(gprob)
			tprob = float(t_ct/w)
			p.append(tprob)
			h = 0
		for i in range(len(p)):
			h -= p[i] * math.log2(p[i])
			if h < 0.0001:
				h = 0
	return h