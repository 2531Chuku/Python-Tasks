'''
Palindrome checker

write a  python function that checks whether a given string is a palindrome.

___________________________Algorithm________________________

'''

def isPalindrome(userStringInput):
  userStringInput = ''.join(stringChar for stringChar in userStringInput if userStringInput.isalnum()).lower()

  return userStringInput == userStringInput[::-1]



# test cases 
print(isPalindrome("radar"))
print(isPalindrome("percival"))