'''
Team Member #1: Connor Cooley
Zagmail address for team member 1: ccooley@zagmail.gonzaga.edu
Test2a: Forward Algorithm
Due: November 16, 2018
Usage: python test2a.py matA.txt matB.txt sequence
'''

import sys
import csv
import numpy as np
import math

def forwardAlg(matA, matB, givenSequence):
  length = len(givenSequence)
  states = len(matA)
  matrix = np.zeros((states, length))
  probability = 0.0
  for s in range(1, states - 1):
    matrix[s][0] = matA[0][s] * matB[s][givenSequence[0] - 1]
  for t in range(1, length):
    for s in range(1, states - 1):
      total = 0.0
      for i in range(states):
        total += (matrix[i][t - 1] * matA[i][s] * matB[s][givenSequence[t] - 1])
      matrix[s][t] = total
  for s in range(1, states - 1):
    probability += (matrix[s][length - 1] * matA[s][states - 1])
  matrix[states - 1][length - 1] = probability

  return matrix[states - 1][length - 1]
    
def main():
  finA = sys.argv[1]
  finB = sys.argv[2]
  input = sys.argv[3]
  givenSequence = [int(i) for i in input]
  readerA = csv.reader(open(finA, 'rb'), delimiter = ',')
  readerB = csv.reader(open(finB, 'rb'), delimiter = ',')
  a = list(readerA)
  b = list(readerB)
  matA = np.array(a).astype('float')
  matB = np.array(b).astype('float')
  probability = forwardAlg(matA, matB, givenSequence)
  print ("\n")
  print "Probability of your given sequence: ", probability
  print ("\n")
  
main()
