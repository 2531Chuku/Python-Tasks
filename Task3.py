import re

''' 
Develop a Python function  that validate  whether a given string is a valid email address. implement checks for the format, including the presence of an '@' symbol and a domain name

____________________Algorithm_____________
import the module re(regular expression)
user enter the string email which will be evaluated for pattern existence 
return boolean values : true 
'''


def isEmailValid(email):
  pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  return isPatternMatched(pattern, email)


def isPatternMatched(pattern, email):
  if re.match(pattern, email):
    return True
  else:
    return False

# Test cases
print(isEmailValid("percival@gmail.com"))
print(isEmailValid("percival"))
