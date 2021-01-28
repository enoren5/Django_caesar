# caesar.py
# Courtesy of Real Python: https://realpython.com/python-practice-problems/

import string

def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)


print(caesar("abcdefghijklmnopqrstuvwxyz", 3))