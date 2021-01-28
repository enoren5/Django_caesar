# caesar.py
import string

def caesar(plain_text, shift_num):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)


print(caesar("abcdefghijklmnopqrstuvwxyz", 3))

def encrypt(caesar(plain_text, shift_num)):