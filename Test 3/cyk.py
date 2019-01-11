'''
Team Member #1: Connor Cooley
Zagmail address for team member 1: ccooley@zagmail.gonzaga.edu
Test3C: CYK Parser
Due: December 14, 2018
Usage: python cyk.py cfg#.txt strng#.txt
'''

import csv
import numpy as np
import sys

def main():		
	file = sys.argv[1]
	cfg = read(file)
	string = open(sys.argv[2], 'r').read().split()
		
	print cyk(cfg, string)

def read(file):
	cfg = {}
	fopen = open(file, 'r')
	for i in fopen:
		i = i.split()
		key = i[0]
		if not key in cfg:
			cfg[key] = []
		for val in i[2:]:
			cfg[key].append(val)

	return cfg

# CYK Algorithm
def cyk(cfg, string):
	length = len(string)
	matrix = [[[] for x in range(length + 1)] for y in range(length + 1)]
	
	# Diagonal
	for step in range(1, length + 1):
		for key, val in cfg.items():
			if string[step - 1] in val:
				matrix[step][step].append(key)
			
	# Fill Matrix
	for i in range(2, length + 1):
		for j in range(1, length - i + 2):
			for k in range(j, j + i - 1):
				for l in matrix[j][k]:
					for m in matrix[k + 1][j + i - 1]:
						for key, val in cfg.items():
							if l + '+' + m in val:
								matrix[j][j + i - 1].append(key)
								
	if ("S" in matrix[1][length]):
		return "YES"
	else:
		return "NO"
		
main()