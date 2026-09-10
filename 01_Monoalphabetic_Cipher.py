

import string

plain = string.ascii_uppercase
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"


def encrypt(text):
    result = ""

    for ch in text.upper():
        if ch in plain:
            result += cipher[plain.index(ch)]
        else:
            result += ch

    return result


def decrypt(text):
    result = ""

    for ch in text.upper():
        if ch in cipher:
            result += plain[cipher.index(ch)]
        else:
            result += ch

    return result


message = input("Enter the message: ")

encrypted = encrypt(message)
decrypted = decrypt(encrypted)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
