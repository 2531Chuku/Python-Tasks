import random
'''
create a number guessing game where the program generate a random number between specified range and the user tries to guess. it provide the  feedback  to the user if their guess is too high or low

_________________________________Algorithms__________________________________________


'''

def number_guessing_game():
    print("Welcome to the number guessing game.")
    prompt_user_to_enter_range()
    

def play_game(number_to_guess, tries):
  while True:
      try:
          user_guess = int(input("Take a guess: "))
          tries += 1
          
          if user_guess < number_to_guess:
              print("Too low!")
          elif user_guess > number_to_guess:
              print("Too high!")
          else:
              print(f"Congratulations! You guessed the number {number_to_guess} in {tries} tries.")
              break
      except ValueError:
          print("That's not a valid number. Please enter a valid integer.")


def prompt_user_to_enter_range():
  while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            
            if lower_bound >= upper_bound:
                print("The lower bound must be less than the upper bound. Please try again.")
                continue
            
            number_to_guess = random.randint(lower_bound, upper_bound)
            tries = 0
            
            print(f"I have picked a number between {lower_bound} and {upper_bound}. Can you guess it?")
            
            play_game(number_to_guess,tries)
            prompt_user_to_play_again()
        
        except ValueError:
            print("That's not a valid number. Please enter integers for the range.")


def prompt_user_to_play_again():
  play_again = input("Do you want to play again? (yes/no): ").strip().lower()
  if play_again != 'yes':
      print("Thank you for playing! Goodbye!")
      return


if __name__ == "__main__":
    number_guessing_game()
