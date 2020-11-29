# Sourced from here: https://python-forum.io/Thread-Learning-Python-with-a-Caesar-cipher?pid=131456#pid131456
# Modified by Drone4four

import string
   
def encrypt(message, shift=0, replace='', alphabet=string.ascii_letters):
    reply = ''
    for letter in message:
        try:
            position = alphabet.index(letter) # Get ord value of letter in alphabet
            position = (position+shift) % len(alphabet) # Shift ord value
            reply += alphabet[position] # Convert shifted ord value back to a letter
        except:
            reply += replace # Use replace for letters not found in alphabet
    return reply
 
message = "Hello World"
encrypted = encrypt(message, shift=1, replace=' ')
decrypted = encrypt(encrypted, shift=-2, replace=' ')
print(encrypted)
print(decrypted)