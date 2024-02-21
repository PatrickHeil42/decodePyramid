# decodePyramid
Repository code to solve pyramid code problem for job application question.

# Problem given:
We are given a text file of format: 
3 love
6 computers
2 dogs
4 cats
1 I
5 you
We want to imagine this in a pyramid format, with each value being added (in order), 
  1
 2 3
4 5 6
And then grab the right side values for the message
1, 3 ,6
or 
I love computers

So with our text file I want to read the data into a list of paired values. 
listOfPairedValues [Int | String]. 
*Need to double check value type and format for python.*
Can be done with:
      for each loop that's going line by line of input.text
      (Each "line" is a word in the text file.)
            Code to split this line into key value pair : Number | Word    
            Code to enter this line into listOfPairedValues. Append?
          
To "construct" the pyramid in python, we can make our list again in order, divy it into levels (cutting off any leftover values), and then grab the right side values
with this formula. n = index number of word.

# Pyramid Formulas
      - n = pyramid level +1 going from 1 at 1 up. 
      - Number of pyramid levels = (NumberOfLines) / (0.5* n *(n+1))
      - Level = 0.5 * n *(n+1) 
         *** Pattern/formula from using this link: https://www.wolframalpha.com/widgets/view.jsp?id=a3af2e675c3bfae0f2ecce820c2bef43       

# Implementation 

