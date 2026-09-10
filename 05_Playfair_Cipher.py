

def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    text = ""

    for ch in key + alphabet:
        if ch in alphabet and ch not in text:
            text += ch

    matrix = [text[i:i + 5] for i in range(0, 25, 5)]

    return matrix


def find_position(matrix, ch):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == ch:
                return row, col


def prepare_text(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    text = text.replace("J", "I")

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            result += a + "X"
            i += 1
        elif text[i] == text[i + 1]:
            result += a + "X"
            i += 1
        else:
            result += a + text[i + 1]
            i += 2

    return result


def process_pair(a, b, matrix, decrypt=False):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)

    shift = -1 if decrypt else 1

    if r1 == r2:
        return (
            matrix[r1][(c1 + shift) % 5] +
            matrix[r2][(c2 + shift) % 5]
        )

    elif c1 == c2:
        return (
            matrix[(r1 + shift) % 5][c1] +
            matrix[(r2 + shift) % 5][c2]
        )

    else:
        return matrix[r1][c2] + matrix[r2][c1]


def encrypt(text, key):
    matrix = create_matrix(key)
    text = prepare_text(text)

    result = ""

    for i in range(0, len(text), 2):
        result += process_pair(
            text[i], text[i + 1], matrix
        )

    return result


def decrypt(text, key):
    matrix = create_matrix(key)

    result = ""

    for i in range(0, len(text), 2):
        result += process_pair(
            text[i], text[i + 1], matrix, True
        )

    return result


key = input("Enter the key: ")
message = input("Enter the message: ")

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
