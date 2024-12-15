import re

'''
create  a python function  that evaluate  the strength of the password entered by the user implement checks for factors such as  lowercase letters, digits and special characters


_________________________________Algorithms__________________________________
'''



def evaluate_password_Strength(password):
  password_strength = "weak"
  suggestions = []

  search_Password_for_pattern(suggestions, password)
  prompt_user_about_password_length(password)
  update_user_about_password_strength(suggestions)
  return {
    "password_strength" : password_strength,
    "Suggestions" : suggestions
  }
  

# Code need to dry
def search_Password_for_pattern(suggestions,password):
  if not re.search("[a-z]", password):
    suggestions.append("Add lowercase letters to your password")
  if not re.search("[A-Z]", password):
    suggestions.append("Add uppercase letters to your password")
  if not re.search("[0-9]", password):
    suggestions.append("Add digits to your password")
  if not re.search("[^A-Za-z0-9]", password):
    suggestions.append("Add special characters  to your password")



def prompt_user_about_password_length(password):
  if len(password) < 8:
    print("make your password 8 characters long")

def update_user_about_password_strength(suggestions):
  if len(suggestions) == 0:
    password_strength = "Strong"
  elif len(suggestions) <= 2:
    password_strength = "good"

def output():
  password = input("Please enter a password : ")
  result = evaluate_password_Strength(password)

  print(f"Password strength : {result['password_strength']}")
  if result['Suggestions']:
    print("Suggestions for improvement")
    for suggestion in result['Suggestions']:
      print(f"-{suggestion}")

output()