'''
Team Member #1: Connor Cooley
Team Member #2: N/A
Zagmail address for team member 1: ccooley@zagmail.gonzaga.edu
Project 2: This project counts the number of substrings in a file and displays
                the number to the user
Due: September 7, 2018
'''

def my_open():
    print ("This program will ask you to enter the name of an existing file.")
    print ("Be sure to put quotation marks around the file name")
    while(True):
        fin = input('Enter an input file name\n')
        try:
            fin = open(fin, 'r')
            break
        except:
            print("Invalid file name.  Try again.")
    return fin

def read_file_as_string(fin):
    string = fin.read()
    return (string)
    
def searchSub(string,subStr,posStr_in):
    posSub = 0
    posStr = posStr_in
    while(posSub < len(subStr)):
        if string[posStr] == subStr[posSub]:
            posSub = posSub + 1
            posStr = posStr + 1
        else:
            return 0
    return 1

def findPos(string,subStr):
    count = 0
    posStr = 0
    lastSub = len(string) - len(subStr)

    while (posStr <= lastSub):
        count += searchSub(string,subStr,posStr)
        posStr = posStr + 1
        if posStr > lastSub + 1:
            print "substring not found"
    return count

def main():
    fin = my_open()
    string = read_file_as_string(fin)
    subStr = input("Enter a substring\n")
    output = findPos(string,subStr)
    print output
    fin.close
    
    

main()

   


