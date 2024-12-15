import random
''' write a python program that generate a random number between 1 and 100. the user should then try to guess the number. the program  should provide hints such as  too high or two low until the correct number is guessed 


___________________________Algorithms__________________________________


'''

def guess_the_number():
  number_to_guess = random.randint(1,100)
  attempts = 0
  handlingError(number_to_guess, attempts)

    
def handlingError(number_to_guess, attempts):
  while True:
    user_guess = input("User take a guess : ")
    user_quit_guessing_number(user_guess,number_to_guess)
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("That's not a valid number!")
        continue
    attempts += 1
    compliment_user(user_guess , number_to_guess, attempts)

def user_quit_guessing_number(user_guess, number_to_guess):
  if user_guess.lower() == 'quit':
      print("Okay, the number was {}.".format(number_to_guess))
  return


def compliment_user(user_guess , number_to_guess, attempts):
  if user_guess == number_to_guess:
      print("Congratulations! You found the number in {} attempts.".format(attempts))
      return
  elif user_guess < number_to_guess:
    print("Too low!")
  else:
    print("Too high!")

# invoke 
guess_the_number()

