# First sample code from Tutorials Point (whcih I ported from Python 2 to Python 3): https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm

def encrypt(text,variance):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + variance-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + variance - 97) % 26 + 97)
        return result

text = "CEASER CIPHER DEMO"
variance = 4

print(f"Plain Text {text}")
print(f"Shift pattern : {str(variance)}")
print(f"Cipher: {encrypt(text,variance)}")
