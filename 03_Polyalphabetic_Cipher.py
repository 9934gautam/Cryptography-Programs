

def encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            j += 1
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            j += 1
        else:
            result += ch

    return result


message = input("Enter the message: ")
key = input("Enter the key: ")

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
