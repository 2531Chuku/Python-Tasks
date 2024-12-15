'''
write a python function  that generate the fibonacci sequence  up to a given  number of terms. the function  should take  an integer input  from the user  and display  the fibonacci sequence  up to  that number of terms

________________________________Algorithms_____________________________________

'''

def handleError():
  while True:
    try:
      num_terms = int(input("Enter number of terms : "))
      if num_terms <= 0:
        print("Please enter a positive integer")
      else:
        break
    except ValueError:
      print("That's not a valid number")
  return num_terms

def performOperations(fibonacci_sequence , num_terms):
  while len(fibonacci_sequence) < num_terms:
    next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_term)


def generate_fibonacci_sequence():
  num_terms = handleError()
  fibonacci_sequence = [0,1]
  performOperations(fibonacci_sequence, num_terms)
  print(f"The Fibonacci sequence up to {num_terms} terms is:")
  print(fibonacci_sequence[:num_terms])

# Invoke
generate_fibonacci_sequence()