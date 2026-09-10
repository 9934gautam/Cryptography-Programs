
def get_order(key):
    return sorted(range(len(key)), key=lambda i: (key[i], i))


def columnar_encrypt(text, key):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())

    columns = len(key)
    rows = (len(text) + columns - 1) // columns

    grid = []
    index = 0

    for _ in range(rows):
        row = []

        for _ in range(columns):
            if index < len(text):
                row.append(text[index])
                index += 1
            else:
                row.append('X')

        grid.append(row)

    order = get_order(key)

    result = ""

    for col in order:
        for row in grid:
            result += row[col]

    return result


def columnar_decrypt(cipher, key):
    columns = len(key)
    rows = len(cipher) // columns

    order = get_order(key)

    grid = [[''] * columns for _ in range(rows)]

    index = 0

    for col in order:
        for row in range(rows):
            grid[row][col] = cipher[index]
            index += 1

    result = ""

    for row in grid:
        result += ''.join(row)

    return result.rstrip('X')


def double_encrypt(text, key1, key2):
    first = columnar_encrypt(text, key1)
    second = columnar_encrypt(first, key2)

    return second


def double_decrypt(cipher, key1, key2):
    first = columnar_decrypt(cipher, key2)
    second = columnar_decrypt(first, key1)

    return second


message = input("Enter the message: ")
key1 = input("Enter first key: ")
key2 = input("Enter second key: ")

encrypted = double_encrypt(message, key1, key2)
decrypted = double_decrypt(encrypted, key1, key2)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
