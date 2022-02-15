# Questions of Codebyte.com

# Longest Word
# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567" 

import re

def LongestWord(sen):
  word = ""
  temp = ""
  # code goes here
  new_string = ''.join(filter(lambda x: not x.isdigit(), sen))
  cleanString = re.sub('\W+',' ', new_string)
  
  for letter in cleanString:
    if letter == " ":
      word = ""
    else:
      word += letter
    if len(word) > len(temp):
        temp = word
  
  sen = temp

  return sen
  

# keep this function call here 
print(LongestWord(input()))

# ----------------------------------------------
# First Factorial
# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer. 

def FirstFactorial(num):
  temp = num
  while num != 1:
    num = num - 1     
    temp = temp * num
    
  num = temp 

  # code goes here
  return num

# keep this function call here 
print(FirstFactorial(input()))

# ----------------------------------------------
# First Reverse
# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 

def FirstReverse(strParam):

  # code goes here
  temp = []
  for l in strParam:
    temp.insert(0,l)
  reverse = ''
  for x in temp:
    reverse += x
  strParam = reverse
  
  return strParam

# keep this function call here 
print(FirstReverse(input()))

#Much more simple version, didn't realise you could do this.

def FirstReverse(strParam):

  strParam = strParam[::-1]
  return strParam

# keep this function call here 
print(FirstReverse(input()))

# ----------------------------------------------
# Find Intersection
# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false. 

def FindIntersection(strArr):

  item1 = []
  item2 = []
  temp = ""
  inter = ""
  # code goes here
  count = 0
  for item in strArr:
    item =item.replace(' ', '')
    for x in item:
      if x == ",":
        if count == 0:
          item1.append(temp)
        if count == 1:
          item2.append(temp)
        temp = ""
      else:
        temp += x
    if count == 0:
          item1.append(temp)
    if count == 1:
      item2.append(temp)
    temp = ""
      
    count += 1

  for x in item1:
    for y in item2:
      if x == y:
        if len(inter) == 0:
          inter = x
        else:
          inter += "," + x
  return inter

# keep this function call here 
print(FindIntersection(input()))

# ----------------------------------------------
# Bracket Combinations
# Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, and return the number of valid combinations that can be formed with num pairs of parentheses. For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). There are 5 total combinations when the input is 3, so your program should return 5. 

import math

def BracketCombinations(num):

  # code goes here
  return int(math.factorial(2 * num) / (math.factorial(num + 1) * math.factorial(num)))

# keep this function call here 
print(BracketCombinations(input()))
# ----------------------------------------------
