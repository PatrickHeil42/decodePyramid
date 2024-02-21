# decodePyramid
Repository code to solve pyramid code problem for job application question.

# Problem given:
We are given a text file of format: 


From this we want to read the data into a list of paired values. 
listOfPairedValues [Int | String]. Need to double check value type and format for python.
Can be done with:
      for each loop that's going line by line of input.text
            Code to split this line into key value pair : Number | Word    
            Code to enter this line into listOfPairedValues. Append?
          
  Instead of constructing the pyramid in python we can make our list in order, and grab
  the value + number of levels There Would be with this input. 
  formula 
          (Number of lines from count function). Each line is a word in the text file.
           Number of pyramid levels = NumberOfLines /(0.5*N*(n+1)).
           Level = 0.5 * n *(n+1) 
           n = pyramid level +1 going from 1 at 1 up. 
           
         *** Pattern/formula from using this link: https://www.wolframalpha.com/widgets/view.jsp?id=a3af2e675c3bfae0f2ecce820c2bef43       

    Now we need to calculate the number of levels of the pyramid and iterate through that loop.
    """
