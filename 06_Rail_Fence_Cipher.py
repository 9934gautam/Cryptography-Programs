

def encrypt(text, rails):
    if rails == 1:
        return text

    fence = [""] * rails
    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)


def decrypt(cipher, rails):
    if rails == 1:
        return cipher

    pattern = []
    row = 0
    direction = 1

    for _ in cipher:
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    counts = [pattern.count(i) for i in range(rails)]

    rails_data = []
    start = 0

    for count in counts:
        rails_data.append(list(cipher[start:start + count]))
        start += count

    result = ""

    for r in pattern:
        result += rails_data[r].pop(0)

    return result


message = input("Enter the message: ")
rails = int(input("Enter the number of rails: "))

encrypted = encrypt(message, rails)
decrypted = decrypt(encrypted, rails)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
