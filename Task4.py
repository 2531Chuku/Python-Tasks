
'''
Calculator program

Create a  python program that acts as a basic calculator. it should prompt the user to enter tWo numbers and  an operator(+,-,/,%,*) and then display the results of the operation

___________________Algorithm_______________________

'''


def calculator():
  print("Instructions:\n Choices : 1,2,3,4,5 \n \n 1 is for Addition \n 2 is for Subtraction \n 3 is for Multiplication \n 4 is for Division \n 5 is for Modulus \n ")

  userChoice = int(input("Enter your choice (1/2/3/4/5): "))
  promptUser_for_choices(userChoice)


def promptUser_for_choices(userChoice):
  if userChoice in (1,2,3,4,5):
    number1, number2, operator =twoOperand()
    operationResults(userChoice, operator,number1, number2)
  else:
    print("Invalid Choice")
    promptUser_about_Continuing_using_Calculator()


def twoOperand():
  number1 = float(input("Enter first number : "))
  number2 = float(input('Enter second number : '))
  operator = input("Enter the operator : ")
  return number1, number2, operator



def operationResults(userChoice, operator, number1, number2):
  if userChoice == 1 and operator == "+":
      print(number1, "+", number2,"=", sum_operation(number1, number2))
  elif userChoice == 2 and operator == "-":
    print(number1, "-" , number2,"=", difference_operation(number1, number2))
  elif userChoice == 3 and operator == "*":
    print(number1, "*", number2,"=", product_operation(number1, number2))
  elif userChoice == 4 and operator == "/":
      divide_by_zero(number1, number2)
  elif userChoice == 5 and operator == "%":
      print(number1, "%", number2,"=", remainder_operation(number1, number2))


def divide_by_zero(number1, number2):
  if number2 != 0:
    print(number1, "/", number2,"=", division_operation(number1, number2))
  else:
    print("Error!, Division by zero is not allowed")


def promptUser_about_Continuing_using_Calculator():
  userContinue = input("Do you want to continue? (yes/no):")
  if userContinue.lower() == 'yes':
    calculator()
  else:
    print("Have a good day")

def sum_operation(value, value2):
  return value + value2

def difference_operation(value, value2):
  return value - value2

def division_operation(value, value2):
  return value / value2

def product_operation(value, value2):
  return value * value2

def remainder_operation(value, value2):
  return value % value2

calculator()

