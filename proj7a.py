'''
Phillip Fishburn
pfishburn@zagmail.gonzaga.edu

Connor Cooley
ccooley@zagmail.gonzaga.edu

Project 7: Shakespeare grams
Due: 11/9/18
Usage: python proj7a.py
'''

import pickle
import re

def tokenize():
  file = open('shakespeare.txt', 'r')
  input = file.read().splitlines()  
  input = [re.findall(r'[a-zA-Z\']+', inp) for inp in input]
  input = [[letters.lower() for letters in inp] for inp in input]

  return input
   
def probabilityFunction(frequency):
  last = 0
  probability = []
  for i in frequency:
    probability.append((i[0], i[1] + last))
    last = last + i[1]
  return probability
  
def dictionary(input, number):
  dictionary = {}
  sum = 0
  for inp in input:
    inp = ['<s>'] + inp + ['</s>']
    for i in range(len(inp) - number + 1):
      key = tuple(inp[i + j] for j in range(number))
      sum = sum + 1
      if key in dictionary:
        dictionary[key] = dictionary[key] + 1
      else:
		dictionary[key] = 1
  return dictionary, sum
  
def unigramFunction(clean):
  unigram = {}
  uniTotal = 0
  for i in clean:
    for word in i:
	  uniTotal = uniTotal + 1
	  if word in unigram:
	    unigram[word] = unigram[word] + 1
	  else:
	    unigram[word] = 1
  return unigram, uniTotal
  
def main():
  clean = tokenize()
  unigram, uniTotal = unigramFunction(clean)
		
  bigram, biTotal = dictionary(clean, 2)
  trigram, triTotal = dictionary(clean, 3)
  quadgram, quadTotal = dictionary(clean, 4)
  
  bigramFrequency = [(key, float(item) / biTotal) for key, item in bigram.items()]
  trigramFrequency = [(key, float(item) / triTotal) for key, item in trigram.items()]
  quadgramFrequency = [(key, float(item) / quadTotal) for key, item in quadgram.items()]
  unigramFrequency = [(key, float(item) / uniTotal) for key, item in unigram.items()]
  
  probability = []
  probability.append(probabilityFunction(bigramFrequency))
  probability.append(probabilityFunction(trigramFrequency))
  probability.append(probabilityFunction(quadgramFrequency))
  probability.append(probabilityFunction(unigramFrequency))
  
  fout = open('proj7b.pkl', 'wb')
  pickle.dump(probability, fout)
  fout.close()
  
main()