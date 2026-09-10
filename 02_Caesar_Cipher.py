

def encrypt(text, shift):
    result = ""

    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += ch

    return result


def decrypt(text, shift):
    result = ""

    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += ch

    return result


message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
