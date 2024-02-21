## Code written by Patrick Heil 02/21/2024
## Program to solve pyramid problem for Data Annotation's job assessment.
## See readme for problem details beyond in-line coments. 
import re
from time import sleep

def count():
    
    pathToFile = "coding_qual_input.txt"
    print("Counting: " + pathToFile)
    f = open("coding_qual_input.txt", "r")
    #print(f.readlines())
    text = f.readlines()
    numberOfLines = 0
    for line in text:
            numberOfLines += 1
      
    print("This input has " + str(numberOfLines) + " words in total.")
    return numberOfLines

def read():
    pathToFile = "coding_qual_input.txt"
    f = open("coding_qual_input.txt", "r")
    text = f.readlines()
    i=0
    numberOfLines = count()
    messageList[] = 
    while i < numberOfLines:
        

        
    print(lines)
    
    return lines
'''     
f(n)= 0.5 * n *(n+1)
with n = pyramid level +1. 
'''
'''
def orderList(unorderedList[]) :
    orderedList = []
    for i : unorderedList[]
        
    
    return orderedList
'''
def decode():
        pathToFile = "coding_qual_input.txt"
        count()
        wordListUnordered = read()
        #orderedList = orderList(wordListUnordered)
        message = "test"
        ##message.append("Test")
        #for i, line in enumerate(fileText):
        #pairs = line.strip().split()
        print(message)
        return message
        ##def decode(file)
#pathToFile = "c:\\Users\\Pat\\Desktop\\ai.job\\coding_qual_input.txt"
pathToFile = "coding_qual_input.txt"

#file = open(pathToFile, 'r')
decode()