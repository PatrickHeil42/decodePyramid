## Code written by Patrick Heil 02/21/2024
## Program to solve pyramid problem for Data Annotation's job assessment.
## See readme for problem details beyond in-line coments. 
import re
from time import sleep

def count(file):
    
    print("Decoding " + pathToFile)
    myFile = open(pathToFile, 'r')
    text = myFile.read(myFile) 
    numberOfLines = 0
    for character in text:
        if character == "\n":
            numberOfLines = numberOfLines + 1
    return "This input has " + numberOfLines + "."
def read(file):
    myFile = open(pathToFile, 'r')
    text = myFile.read(myFile)
    lines = myFile.readlines()
    print(lines)
     ##for character in text:
      ##  if character == "\n":
      ##       print
    return lines
'''     
f(n)= 0.5 * n *(n+1)
with n = pyramid level +1. 
'''
def decode(fileName):
        print(numberOfLines = count(fileName))
        print(fileText = read(fileName))
        decoded_words = []
        message = "test"
        ##message.append("Test")
        for i, line in enumerate(fileText):
            pairs = line.strip().split()
        return message
        ##def decode(file)
pathToFile = "c:\\Users\\Pat\\Desktop\\ai.job\\coding_qual_input.txt"
#file = open(pathToFile, 'r')
print(decode(pathToFile))