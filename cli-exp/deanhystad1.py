# Sourced from here: https://python-forum.io/Thread-Learning-Python-with-a-Caesar-cipher?pid=131456#pid131456

import string
   
def encrypt(message, shift=0, replace='', alphabet=string.ascii_letters):
    reply = ''
    for letter in message:
        try:
            # Get ord value of letter in alphabet
            index = alphabet.index(letter)
            # Shift ord value
            index = (index+shift) % len(alphabet)
            # Convert shifted ord value back to a letter
            reply += alphabet[index]
        except:
            reply += replace # Use replace for letters not found in alphabet
    return reply
 
message = input('Message to encrypt: ')
encrypted = encrypt(message, shift=8, replace=' ')
decrypted = encrypt(encrypted, shift=-8, replace=' ')
print(encrypted)
print(decrypted)