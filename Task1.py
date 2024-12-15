'''
Create a Python function that takes a string as input and return the reverse of that string

________________Algorithms Explanation___________________

Since the colon ":" means start at the beginning and go to the end
To step backwards each time for every character , it uses -1
To extract the characters from string, method slice() is ideal

Inputs: string
Output: string
variable: (stringReversal : function) and userStringInput
Test Data:
Nationality => string => ytilanoitaN
Hello => string => olleH

Event and action:
invoke stringReversal() => return reversed string

algorithm
userStringInput -> start from beginning to end of string
slice the method 
step: -1


___End Results 
When the user provide a string, that string will be returned backward

'''

def stringReversal(userStringInput):
  return userStringInput[::-1]


# Test cases
print(stringReversal("Nationality"))
print(stringReversal("Application"))


