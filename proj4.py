'''
Team Member #1: Connor Cooley
Zagmail address for team member 1: ccooley@zagmail.gonzaga.edu
Project 2: This program executes the soundex algorithm
Due: September 28, 2018
usage: python proj4.py input
'''

import sys

'''
pre: input is a string
post: first letter is removed then capitalized
'''
def stepOne(input):
  firstLetter = input[0]
  return firstLetter.upper()
	
'''
pre: input is a string
post: adjacent identical letters are removed starting after the first letter
'''
def stepThree(number):
  noAdjacent = ''
  currentChar = number[1]
  noAdjacent = noAdjacent + currentChar
  for char in number[2:]:
    if not (char == currentChar):
	  noAdjacent = noAdjacent + char
    currentChar = char
  return noAdjacent
    
'''
pre: input is a string
post: returns a string without the letters that are
        supposed to be removed in the soundex algorithm
'''
def stepFour(noAdjacent):
  removed = ''
  for char in noAdjacent[0:]:
    if not (char == 'a' or char == 'e' or char == 'h' or char == 'i' \
    or char == 'o' or char == 'u' or char == 'w' or char == 'y'):
      removed = removed + char
  return removed

'''
pre: removed is a string returned from stepTwo
post: letters are replaced with numbers
'''
def stepTwo(input):
  number = ''
  for char in input:
    if (char == 'b' or char == 'f' or char == 'p' or char == 'v'):
      number = number + '1'
    elif (char == 'c' or char == 'g' or char == 'j' or char == 'k' \
    or char == 'q' or char == 's' or char == 'x' or char == 'z'):
      number = number + '2'
    elif (char == 'd' or char == 't'):
      number = number + '3'
    elif (char == 'l'):
      number = number + '4'
    elif (char == 'm' or char == 'n'):
      number = number + '5'
    elif (char == 'r'):
      number = number + '6'
    else:
	  number = number + char
  return number


'''
pre: takes the first letter and adds on the numbers
post: adds on 0's to make numbers 3 digits long if needed
         returns the firstLetter with the numbers added on
'''
def stepFive(firstLetter, removed):
  if len(removed) > 3:
    removed = removed[:3]
  if len(removed) == 0:
    removed = removed + '000'
  if len(removed) == 1:
    removed = removed + '00'
  if len(removed) == 2:
    removed = removed + '0'
  return firstLetter + removed

'''
pre: stores the string entered by the user into argv[1]
post: prints the entered string in soundex form
'''
def main():
  input = sys.argv[1]
  output = stepFive(stepOne(input),stepFour(stepThree(stepTwo(input))))
  print input + '->' + output
	
main()