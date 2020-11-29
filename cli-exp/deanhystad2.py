# Sourced from here: https://python-forum.io/Thread-Learning-Python-with-a-Caesar-cipher?pid=131456#pid131456
# This is the raw original copy verbatim from deanhystad
 
import string
   
def encrypt(message, shift=0, replace='', alphabet=string.ascii_letters):
    # Define the input-output replacement map
    size = len(alphabet)
    code = {a:alphabet[(index+shift) % size] for index, a in enumerate(alphabet)}
    # Encrypt the message using the replacement map
    return ''.join([code.get(letter, replace) for letter in message])
 
message = "Hello World"
encrypted = encrypt(message, shift=8, replace=' ')
decrypted = encrypt(encrypted, shift=-8, replace=' ')
print(encrypted)
print(decrypted)