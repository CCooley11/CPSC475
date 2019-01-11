'''
Team Member #1: Connor Cooley
Zagmail address for team member 1: ccooley@zagmail.gonzaga.edu
Project 5: Minimum Edit Distance
Due: October 5, 2018
usage: python proj5.py source target
'''

import sys

def minEditDistance(source, target):
  rows = len(source)
  cols = len(target)
  if rows < 1:
    return cols
  if cols < 1:
    return rows
	
  dist = [[0 for i in range(0, cols + 1)] for k in range(0, rows + 1)]
  ptr = [[[" " for j in range(0, 3)] for i in range(0, cols + 1)] for k in range(0, rows + 1)]
  dist[0][0] = 0
  
  for i in range(1, rows + 1):
    dist[i][0] = dist[i - 1][0] + 1
    ptr[i][0][0] = "u"
  for j in range(1, cols + 1):
    dist[0][j] = dist[0][j - 1] + 1
    ptr[0][j][2] = "l"
        
  for i in range(1, rows + 1):
    for j in range(1, cols + 1):
      if source[i - 1] == target[j - 1]:
        cost = 0
      else:
        cost = 2
	  
      delete = dist[i - 1][j] + 1
      insert = dist[i][j - 1] + 1
      substitute = dist[i - 1][j - 1] + cost
      dist[i][j] = min(delete,      
                           insert,      
                           substitute) 
				
      smallest = dist[i][j]
      if smallest == delete:
        ptr[i][j][0] = "u"
      if smallest == insert:
        ptr[i][j][2] = "l"
      if smallest == substitute:
        ptr[i][j][1] = "d"	
    
  return dist, ptr
  
def alignment(table, ptr, i, j, s, source, target):
  if i == 0 and j == 0:
    return s
	
  sTemp = s
  
  if ptr[i][j][1] == "d":
    if i != 0 and j != 0 and source[i - 1] == target[j - 1]:
      sTemp = "n" + s
    else:
      sTemp = "s" + s
	  
    return alignment(table, ptr, i - 1, j - 1, sTemp, source, target)
  else:	
    if ptr[i][j][0] == "u":
      if ptr[i][j][2] == "l" and table[i][j - 1] <= table[i - 1][j]:
        sTemp = "i" + s
        return alignment(table, ptr, i, j - 1, sTemp, source, target)
      else:		
        sTemp = "d" + s
        return alignment(table, ptr, i - 1, j, sTemp, source, target)
    elif ptr[i][j][2] == "l":
      sTemp = "i" + s
      return alignment(table, ptr, i, j - 1, sTemp, source, target)
	  
def printAlignment(alignmentString, source, target):
  aString = ""
  out = ""
  i = 0
  
  for s in alignmentString:
    if s == "s" or s == "i" or s == "d":
      aString = aString + s + " "
    else:
      aString = aString + "  "
    if s == "i":
      out = out + "* "
    else:
      out = out + source[i] + " "
      i = i + 1
  print out
  
  out = ""
  i = 0
  for s in alignmentString:
    out = out + "| "
  print out
  
  out = ""
  i = 0
  for s in alignmentString:
    if s == "d":
      out = out + "* "
    else:
      out = out + target[i] + " "
      i = i + 1
  print out
  print aString
  
def printFinal(table, ptr, source, target):
  alignmentString = ""
  alignmentString = alignment(table, ptr, len(source), len(target), alignmentString, source, target)
  print ""
  printAlignment(alignmentString, source, target)
	  
def main():
  source = sys.argv[1]
  target = sys.argv[2]
  dist, ptr = minEditDistance(source, target)
  print ""
  print "Minimum Edit Distance: " + str(dist[len(source)][len(target)])
  print ""
  print "Alignment: "
  printFinal(dist, ptr, source, target)
  print ""
  
main()