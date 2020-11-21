# As discussed here: https://python-forum.io/Thread-Caesar-cipher?page=2
 
from collections import deque
import string
  
def encrypt(text,shift_variance):
    '''
    INPUT: text as a string and an integer for the shift value.
    OUTPUT: The shifted text after being run through the Caesar cipher.
    ''' 
    original = string.ascii_lowercase # Initializing alphabet variable
    original = deque(list(original)) # Turning the original alphabet into a list
    shifted = original.copy() # Assigning new variable to copy of original alphabet
    shifted.rotate(shift_variance) # Rotating new shifted alphabet 
    original = ''.join(original) # Re-concatenating split list (alphabet)
    shifted = ''.join(shifted)
    text = text.split() # Convert text to list of words
    scrambled_text =[] # Initializing output variable 
    for index, character in enumerate(text[:][:]):
        lookup_index = original.find(character)
        new_character = shifted[lookup_index]
        scrambled_text.append(new_character)
    text = ''.join(text)
    scrambled_text = ' '.join(scrambled_text)

print(encrypt("Hello World", 2))