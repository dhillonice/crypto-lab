from substitution_cipher import generate_key, encrypt
from cryptanalysis import (
    frequency_analysis,
    word_frequency_analysis,
    pattern_analysis,
    recover_key,
    apply_substitution,
    display_partial_plaintext,
    verify_solution
)


def main():

    with open("attacks/substitution_cipher_attack/testcases/plaintext.txt", "r") as file:
        plaintext = file.read()

    key = generate_key()
    ciphertext = encrypt(plaintext, key)

    print("MONOALPHABETIC SUBSTITUTION CIPHER")
    print("==================================")

    print("\nSubstitution Key:")
    for a, b in key.items():
        print(f"{a} -> {b}")

    print("\nCiphertext:")
    print(ciphertext)

    frequency_analysis(ciphertext)

    word_frequency_analysis(ciphertext)

    pattern_analysis(ciphertext)

    recovered_key = recover_key(ciphertext)

    print("\nRecovered Key:")
    for a, b in recovered_key.items():
        print(f"{a} -> {b}")

    partial_plaintext = display_partial_plaintext(
        ciphertext,
        recovered_key
    )

    print("\nRecovered Plaintext:")
    print(partial_plaintext)

    encryption_key = {
        plaintext_char: cipher_char
        for cipher_char, plaintext_char in recovered_key.items()
    }

    print("\nVerification:")
    verify_solution(
        partial_plaintext,
        ciphertext,
        encryption_key
    )


if __name__ == "__main__":
    main()
