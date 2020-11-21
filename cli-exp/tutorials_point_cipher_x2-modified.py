# Second sample code from Tutorials Point: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
import string

message = 'Hello World' #encrypted message
LETTERS = string.ascii_letters


def encrypt(message, LETTERS):
    for key in range(len(LETTERS)):
        translated = ''
        for character in message:
            if character in LETTERS:
                num = LETTERS.find(character)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + character
    return translated

print(f"Encrypted message : {encrypt(message, LETTERS)}")