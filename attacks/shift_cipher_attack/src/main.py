import os

from shift_cipher import encrypt, decrypt
from brute_force_dictionary import (
    load_dictionary,
    brute_force_dictionary
)
from chi_square_attack import chi_square_attack


def main():

    print("=" * 60)
    print("SHIFT CIPHER CRYPTANALYSIS")
    print("=" * 60)

    plaintext = input("\nEnter plaintext: ")

    key = int(input("Enter encryption key (0-25): "))

    ciphertext = encrypt(plaintext, key)

    print("\nCiphertext:")
    print(ciphertext)

    print("\n" + "=" * 60)
    print("DICTIONARY SCORING ATTACK")
    print("=" * 60)

    current_dir = os.path.dirname(os.path.abspath(__file__))

    dictionary_path = os.path.join(
        current_dir,
        "..",
        "dictionary",
        "english_words.txt"
    )

    dictionary = load_dictionary(dictionary_path)

    (
        dict_key,
        dict_plaintext,
        dict_score,
        dict_results

    ) = brute_force_dictionary(
        ciphertext,
        decrypt,
        dictionary
    )

    print("\nPredicted Key:", dict_key)
    print("Predicted Plaintext:", dict_plaintext)
    print("Dictionary Score:", dict_score)

    print("\n" + "=" * 60)
    print("CHI-SQUARE ATTACK")
    print("=" * 60)

    (
        chi_key,
        chi_plaintext,
        chi_score,
        chi_results

    ) = chi_square_attack(
        ciphertext,
        decrypt
    )

    print("\nPredicted Key:", chi_key)
    print("Predicted Plaintext:", chi_plaintext)
    print("Chi-Square Score:", round(chi_score, 2))

    print("\n" + "=" * 60)
    print("COMPARISON")
    print("=" * 60)

    print("Actual Key:", key)

    print(
        "Dictionary Correct?",
        dict_key == key
    )

    print(
        "Chi-Square Correct?",
        chi_key == key
    )


if __name__ == "__main__":
    main()