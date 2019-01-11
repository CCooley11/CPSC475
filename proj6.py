'''
Phillip Fishburn
pfishburn@zagmail.gonzaga.edu

Connor Cooley
ccooley@zagmail.gonzaga.edu

Project 6: Generates 5 random sentences of 10 words each
			where the first word is capitalized and each	
			sentence ends with a period
Due: 10/26/2018
Usage: python proj6.py
'''

import nltk
import random
  
def main():
  from nltk.corpus import brown
  tmp = brown.sents(categories='editorial')
  new = [[item.encode('ascii') for item in lst] for lst in tmp]
  cleanWords = []
  for sent in new:
    for word in sent:
      tokenWord = tokenize(word)
      if tokenWord is not '':
        cleanWords.append(tokenWord)
  contStr = ' '.join(cleanWords)
  count_dict = freq_table(contStr)
  numOfWords = len(cleanWords)
  printSentences(frequency(count_dict, numOfWords))

# Calculate frequency
def frequency(count_dict, numOfWords):
  rFreq_dict = {}
  for i in count_dict.keys():
    rFreq_dict[i] = count_dict[i]/float(numOfWords)
  z = 0
  for i in count_dict.keys():
    z = z + count_dict[i]
  cProb_dict = {}
  runningTotal = 0
  for i in rFreq_dict.keys():
    runningTotal = runningTotal + rFreq_dict[i]
    cProb_dict[i] = runningTotal
  #print runningTotal
  return cProb_dict

# Print the randomly generated sentences
def printSentences(cProb_dict):
  print
  print
  for sentence in range(5): #5 sentences
    newSent = []
    for word in range(10): #10 words each
      exit = 0
      num = random.randrange(1000000000)/1000000000.0 #random number
  		
      for i in sorted(cProb_dict, key = cProb_dict.get): #first word whose cumulative probability
        if (exit == 0):							       # is more than the random number
          if (cProb_dict[i] >= num):
  			if (word == 0):
  			  i = i.capitalize()
  			if (word == 9):
  			  i = i + '.'
  			newSent.append(i)
  			exit = 1
    for i in newSent:
      print i,
    print
    print

# Change to lower case and take out bad chars	
def tokenize(string_in):
  import re
  string = re.sub('\n',' ', string_in)
  #create a list containing all lower case characters
  good_chars = [chr(value) for value in range(ord('a'),ord('z') + 1,1)]
  good_chars.append(' ')
  string = string.lower()
  new_str = ''
  for ch in string:
    if ch in good_chars:
      if ch is not('.' and '?' and '"' and ',' and '!'):
        new_str = new_str + ch
  return new_str

# Save frequencies of each word  
def freq_table(string_in):
  count_dict = {}
  word_lst = string_in.split()
  for word in word_lst:
    if word in count_dict:
      count_dict[word] = count_dict[word] + 1
    else:
      count_dict[word] = 1
  return count_dict

main()