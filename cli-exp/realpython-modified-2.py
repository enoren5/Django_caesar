# caesar.py
import string

def caesar(plain_text, shift_num):
    letters = string.ascii_lowercase
    try:
        mask = letters[shift_num:] + letters[:shift_num]
    except TypeError:
        print("Please enter an integer (No floats or strings)")
        return caesar(plain_text, shift_num=1)
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)

print(caesar("abcdefghijklmnopqrstuvwxyz", "1.2"))