import re
from collections import Counter

'''
write a python program that read a text file and counts the occurrences of each word in the file. display  the results in alphabetical order along with their respective counts

_______________________________Algorithm_________________________


'''

def count_word_occurrence(filename):
  error_File_handling(filename)

def error_File_handling(filename):
  try:
    open_file(filename) 
  except FileNotFoundError:
      print(f"Sorry, the file '{filename}' does not exist.")
  except Exception as e:
      print(f"An error occurred: {e}")

def open_file(filename):
  with open(filename, 'r') as file:  
    text = file.read()  
    words = re.findall(r'\b\w+\b', text.lower())  
    word_counts = Counter(words) 
    
    print("Word Counts:")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")


# test case and invoke
filename = input("Enter the name of the text file: ")
count_word_occurrence(filename)
