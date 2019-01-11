'''
Team Member #1: Connor Cooley
Zagmail address for team member 1: ccooley@zagmail.gonzaga.edu
Test2a: Viterbi Algorithm
Due: November 30, 2018
Usage: python test2b.py matA.csv matB.csv sequence
'''

import sys
import csv
import numpy as np
import math

def viterbiAlgorithm(matA, matB, givenSequence):
  N = len(matA)
  T = len(givenSequence)
  back = np.zeros((N, T))
  states = []
  final = []
  viterbi = np.zeros((N, T))
  prob = 0.0
  
  for s in range(1, N - 1):
    viterbi[s][0] = matA[0][s] * matB[s][givenSequence[0] - 1]
  for t in range(1, T):
    for s in range(1, N - 1):
      argMax = 0.0
      for last in range(N):
        argMax = max(viterbi[last][t - 1] * matA[last][s] * matB[s][givenSequence[t] - 1], argMax)
        if(viterbi[last][t - 1] * matA[last][s] * matB[s][givenSequence[t] - 1] == argMax):
          back[s][t] = last
      viterbi[s][t] = argMax
  for s in range(1, N - 1):
    prob = max(viterbi[s][T - 1] * matA[s][N - 1], prob)
    if(viterbi[s][T - 1] * matA[s][N - 1] == prob):
      back[N - 1][T - 1] = s
  viterbi[N - 1][T - 1] = prob
  states.append(back[N - 1][T - 1])
  for t in range(T - 1):
    states.append(back[givenSequence[t]][T - t - 1])
  for t in range(T):
    if(states[T - t - 1] == 1):
      final.append('cold')
    else:
      final.append('hot')
	  
  return final
  
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
  sequence = viterbiAlgorithm(matA, matB, givenSequence)
  print ("\n")
  print "Most likely sequence: ", sequence
  print ("\n")
  
main()