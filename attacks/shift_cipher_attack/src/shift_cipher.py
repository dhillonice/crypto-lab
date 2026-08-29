def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                shifted = (ord(char) - ord('A') + key) % 26
                result += chr(ord('A') + shifted)

            else:
                shifted = (ord(char) - ord('a') + key) % 26
                result += chr(ord('a') + shifted)

        else:
            result += char

    return result


def decrypt(text, key):
    return encrypt(text, -key)