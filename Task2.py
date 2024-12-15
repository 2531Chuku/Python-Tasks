'''
create a python program that convert temperatures between Celsius and Fahrenheit
prompt the user to enter a temperature value and the unit of measurement and then display the converted temperature

___________________Algorithm_________________________________
inputs 
output
test data
events and actions
variables 
algorithms 
pseudo

'''
def main():
  print('User is Expected to user this application as follows To convert from Celsius_to_fahrenheit enter value 1, Fahrenheit_to_celsius enter value 2, to Quit use 3 ')

  userChoice = int(input("Please enter your choice(1,2,3) : "))
  userChoices(userChoice)


def Celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def Fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

def fahrenheitConversion():
  celsius = float(input('Enter the temperature in celsius : '))
  fahrenheitTemp = Celsius_to_fahrenheit(celsius)
  print(f"{celsius}°C is equal to {round(fahrenheitTemp,2)}°F ")

def celsiusConversion():
  fahrenheit = float(input('Enter the temperature in fahrenheit : '))
  celsiusTemp = Fahrenheit_to_celsius(fahrenheit)
  print(f"{fahrenheit}°F is equal to {round(celsiusTemp,2)}°C")
  
def userQuit():
  print("Thank you for using our application")

def userChoices(userChoice):
  while True:
    if userChoice == 1:
      fahrenheitConversion()
      break
    elif userChoice == 2:
      celsiusConversion()
      break
    elif userChoice == 3:
      userQuit()
      break
    else:
      print("Invalid choice,Please try again")

# invoke method
main()