
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

BLOCK_SIZE = AES.block_size
oracle_queries = 0


def encrypt_message(plaintext):
    key = get_random_bytes(BLOCK_SIZE)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))
    return key, iv, ciphertext


def create_padding_oracle(key):
    def padding_oracle(iv, ciphertext):
        global oracle_queries
        oracle_queries += 1

        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(ciphertext)
            padding_length = decrypted[-1]

            if padding_length < 1 or padding_length > BLOCK_SIZE:
                return False

            expected_padding = bytes([padding_length]) * padding_length
            return decrypted.endswith(expected_padding)
        except (ValueError, IndexError):
            return False

    return padding_oracle


def recover_block(previous_block, current_block, oracle):
    intermediate = [0] * BLOCK_SIZE
    recovered = bytearray(BLOCK_SIZE)

    for position in range(BLOCK_SIZE - 1, -1, -1):
        padding_value = BLOCK_SIZE - position
        modified = bytearray(previous_block)

        for j in range(position + 1, BLOCK_SIZE):
            modified[j] = intermediate[j] ^ padding_value

        found = False

        for guess in range(256):
            modified[position] = guess
            if oracle(bytes(modified), current_block):
                if position > 0:
                    check = bytearray(modified)
                    check[position - 1] ^= 1
                    if not oracle(bytes(check), current_block):
                        continue

                intermediate[position] = guess ^ padding_value
                recovered[position] = intermediate[position] ^ previous_block[position]
                found = True
                break

        if not found:
            raise RuntimeError("Could not recover a plaintext byte")

    return bytes(recovered)


def padding_oracle_attack(iv, ciphertext, oracle):
    blocks = [
        ciphertext[i:i + BLOCK_SIZE]
        for i in range(0, len(ciphertext), BLOCK_SIZE)
    ]

    recovered = bytearray()

    for index, current_block in enumerate(blocks):
        previous_block = iv if index == 0 else blocks[index - 1]
        recovered.extend(recover_block(previous_block, current_block, oracle))

    return unpad(bytes(recovered), BLOCK_SIZE)


def main():
    global oracle_queries

    plaintext = b"Padding oracle attack demonstration."
    key, iv, ciphertext = encrypt_message(plaintext)
    oracle = create_padding_oracle(key)

    print("Original plaintext:", plaintext.decode())
    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())

    oracle_queries = 0
    recovered = padding_oracle_attack(iv, ciphertext, oracle)

    print("Recovered plaintext:", recovered.decode())
    print("Oracle queries:", oracle_queries)
    print("Recovery successful:", recovered == plaintext)


if __name__ == "__main__":
    main()
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

BLOCK_SIZE = AES.block_size
oracle_queries = 0


def encrypt_message(plaintext):
    key = get_random_bytes(BLOCK_SIZE)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))
    return key, iv, ciphertext


def create_padding_oracle(key):
    def padding_oracle(iv, ciphertext):
        global oracle_queries
        oracle_queries += 1

        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(ciphertext)
            padding_length = decrypted[-1]

            if padding_length < 1 or padding_length > BLOCK_SIZE:
                return False

            expected_padding = bytes([padding_length]) * padding_length
            return decrypted.endswith(expected_padding)
        except (ValueError, IndexError):
            return False

    return padding_oracle


def recover_block(previous_block, current_block, oracle):
    intermediate = [0] * BLOCK_SIZE
    recovered = bytearray(BLOCK_SIZE)

    for position in range(BLOCK_SIZE - 1, -1, -1):
        padding_value = BLOCK_SIZE - position
        modified = bytearray(previous_block)

        for j in range(position + 1, BLOCK_SIZE):
            modified[j] = intermediate[j] ^ padding_value

        found = False

        for guess in range(256):
            modified[position] = guess
            if oracle(bytes(modified), current_block):
                if position > 0:
                    check = bytearray(modified)
                    check[position - 1] ^= 1
                    if not oracle(bytes(check), current_block):
                        continue

                intermediate[position] = guess ^ padding_value
                recovered[position] = intermediate[position] ^ previous_block[position]
                found = True
                break

        if not found:
            raise RuntimeError("Could not recover a plaintext byte")

    return bytes(recovered)


def padding_oracle_attack(iv, ciphertext, oracle):
    blocks = [
        ciphertext[i:i + BLOCK_SIZE]
        for i in range(0, len(ciphertext), BLOCK_SIZE)
    ]

    recovered = bytearray()

    for index, current_block in enumerate(blocks):
        previous_block = iv if index == 0 else blocks[index - 1]
        recovered.extend(recover_block(previous_block, current_block, oracle))

    return unpad(bytes(recovered), BLOCK_SIZE)


def main():
    global oracle_queries

    plaintext = b"Padding oracle attack demonstration."
    key, iv, ciphertext = encrypt_message(plaintext)
    oracle = create_padding_oracle(key)

    print("Original plaintext:", plaintext.decode())
    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())

    oracle_queries = 0
    recovered = padding_oracle_attack(iv, ciphertext, oracle)

    print("Recovered plaintext:", recovered.decode())
    print("Oracle queries:", oracle_queries)
    print("Recovery successful:", recovered == plaintext)


if __name__ == "__main__":
    main()
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

BLOCK_SIZE = AES.block_size
oracle_queries = 0


def encrypt_message(plaintext):
    key = get_random_bytes(BLOCK_SIZE)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))
    return key, iv, ciphertext


def create_padding_oracle(key):
    def padding_oracle(iv, ciphertext):
        global oracle_queries
        oracle_queries += 1

        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(ciphertext)
            padding_length = decrypted[-1]

            if padding_length < 1 or padding_length > BLOCK_SIZE:
                return False

            expected_padding = bytes([padding_length]) * padding_length
            return decrypted.endswith(expected_padding)
        except (ValueError, IndexError):
            return False

    return padding_oracle


def recover_block(previous_block, current_block, oracle):
    intermediate = [0] * BLOCK_SIZE
    recovered = bytearray(BLOCK_SIZE)

    for position in range(BLOCK_SIZE - 1, -1, -1):
        padding_value = BLOCK_SIZE - position
        modified = bytearray(previous_block)

        for j in range(position + 1, BLOCK_SIZE):
            modified[j] = intermediate[j] ^ padding_value

        found = False

        for guess in range(256):
            modified[position] = guess
            if oracle(bytes(modified), current_block):
                if position > 0:
                    check = bytearray(modified)
                    check[position - 1] ^= 1
                    if not oracle(bytes(check), current_block):
                        continue

                intermediate[position] = guess ^ padding_value
                recovered[position] = intermediate[position] ^ previous_block[position]
                found = True
                break

        if not found:
            raise RuntimeError("Could not recover a plaintext byte")

    return bytes(recovered)


def padding_oracle_attack(iv, ciphertext, oracle):
    blocks = [
        ciphertext[i:i + BLOCK_SIZE]
        for i in range(0, len(ciphertext), BLOCK_SIZE)
    ]

    recovered = bytearray()

    for index, current_block in enumerate(blocks):
        previous_block = iv if index == 0 else blocks[index - 1]
        recovered.extend(recover_block(previous_block, current_block, oracle))

    return unpad(bytes(recovered), BLOCK_SIZE)


def main():
    global oracle_queries

    plaintext = b"Padding oracle attack demonstration."
    key, iv, ciphertext = encrypt_message(plaintext)
    oracle = create_padding_oracle(key)

    print("Original plaintext:", plaintext.decode())
    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())

    oracle_queries = 0
    recovered = padding_oracle_attack(iv, ciphertext, oracle)

    print("Recovered plaintext:", recovered.decode())
    print("Oracle queries:", oracle_queries)
    print("Recovery successful:", recovered == plaintext)


if __name__ == "__main__":
    main()
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

BLOCK_SIZE = AES.block_size
oracle_queries = 0


def encrypt_message(plaintext):
    key = get_random_bytes(BLOCK_SIZE)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))
    return key, iv, ciphertext


def create_padding_oracle(key):
    def padding_oracle(iv, ciphertext):
        global oracle_queries
        oracle_queries += 1

        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(ciphertext)
            padding_length = decrypted[-1]

            if padding_length < 1 or padding_length > BLOCK_SIZE:
                return False

            expected_padding = bytes([padding_length]) * padding_length
            return decrypted.endswith(expected_padding)
        except (ValueError, IndexError):
            return False

    return padding_oracle


def recover_block(previous_block, current_block, oracle):
    intermediate = [0] * BLOCK_SIZE
    recovered = bytearray(BLOCK_SIZE)

    for position in range(BLOCK_SIZE - 1, -1, -1):
        padding_value = BLOCK_SIZE - position
        modified = bytearray(previous_block)

        for j in range(position + 1, BLOCK_SIZE):
            modified[j] = intermediate[j] ^ padding_value

        found = False

        for guess in range(256):
            modified[position] = guess
            if oracle(bytes(modified), current_block):
                if position > 0:
                    check = bytearray(modified)
                    check[position - 1] ^= 1
                    if not oracle(bytes(check), current_block):
                        continue

                intermediate[position] = guess ^ padding_value
                recovered[position] = intermediate[position] ^ previous_block[position]
                found = True
                break

        if not found:
            raise RuntimeError("Could not recover a plaintext byte")

    return bytes(recovered)


def padding_oracle_attack(iv, ciphertext, oracle):
    blocks = [
        ciphertext[i:i + BLOCK_SIZE]
        for i in range(0, len(ciphertext), BLOCK_SIZE)
    ]

    recovered = bytearray()

    for index, current_block in enumerate(blocks):
        previous_block = iv if index == 0 else blocks[index - 1]
        recovered.extend(recover_block(previous_block, current_block, oracle))

    return unpad(bytes(recovered), BLOCK_SIZE)


def main():
    global oracle_queries

    plaintext = b"Padding oracle attack demonstration."
    key, iv, ciphertext = encrypt_message(plaintext)
    oracle = create_padding_oracle(key)

    print("Original plaintext:", plaintext.decode())
    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())

    oracle_queries = 0
    recovered = padding_oracle_attack(iv, ciphertext, oracle)

    print("Recovered plaintext:", recovered.decode())
    print("Oracle queries:", oracle_queries)
    print("Recovery successful:", recovered == plaintext)


if __name__ == "__main__":
    main()
