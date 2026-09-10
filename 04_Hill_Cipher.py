
import math


def inverse_matrix(key):
    a, b, c, d = key

    determinant = (a * d - b * c) % 26

    if math.gcd(determinant, 26) != 1:
        return None

    determinant_inverse = pow(determinant, -1, 26)

    return [
        (d * determinant_inverse) % 26,
        (-b * determinant_inverse) % 26,
        (-c * determinant_inverse) % 26,
        (a * determinant_inverse) % 26
    ]


def encrypt(text, key):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())

    if len(text) % 2 != 0:
        text += 'X'

    result = ""

    for i in range(0, len(text), 2):
        x = ord(text[i]) - ord('A')
        y = ord(text[i + 1]) - ord('A')

        a, b, c, d = key

        p = (a * x + b * y) % 26
        q = (c * x + d * y) % 26

        result += chr(p + ord('A'))
        result += chr(q + ord('A'))

    return result


def decrypt(text, key):
    inverse = inverse_matrix(key)

    if inverse is None:
        return "Invalid key"

    return encrypt(text, inverse)


print("Enter 4 values for the 2x2 key matrix:")
print("Example: 3 3 2 5")

key = list(map(int, input("Enter key values: ").split()))

if len(key) != 4:
    print("Please enter exactly 4 values.")
else:
    if inverse_matrix(key) is None:
        print("Invalid key! Determinant must be relatively prime to 26.")
    else:
        message = input("Enter the message: ")

        encrypted = encrypt(message, key)
        decrypted = decrypt(encrypted, key)

        print("Encrypted message:", encrypted)
        print("Decrypted message:", decrypted)
