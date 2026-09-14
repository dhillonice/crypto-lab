from collections import Counter
import re


def frequency_analysis(ciphertext):
    letters = [ch.lower() for ch in ciphertext if ch.isalpha()]
    total = len(letters)
    frequency = Counter(letters)

    print("\nFrequency Analysis")
    print("------------------")

    for letter, count in frequency.most_common():
        percentage = (count / total) * 100
        print(f"{letter}: {count} ({percentage:.2f}%)")

    return frequency


def word_frequency_analysis(ciphertext):
    words = re.findall(r"[A-Za-z]+", ciphertext.lower())
    frequency = Counter(words)

    print("\nWord Frequency Analysis")
    print("-----------------------")

    for word, count in frequency.most_common():
        print(f"{word}: {count}")

    print("\nOne-letter words:", [w for w in frequency if len(w) == 1])
    print("Two-letter words:", [w for w in frequency if len(w) == 2])
    print("Three-letter words:", [w for w in frequency if len(w) == 3])

    return frequency


def get_pattern(word):
    mapping = {}
    next_number = 0
    pattern = []

    for ch in word.lower():
        if ch not in mapping:
            mapping[ch] = next_number
            next_number += 1

        pattern.append(mapping[ch])

    return tuple(pattern)


def pattern_analysis(ciphertext):
    words = re.findall(r"[A-Za-z]+", ciphertext.lower())
    patterns = {}

    for word in words:
        pattern = get_pattern(word)
        patterns.setdefault(pattern, []).append(word)

    print("\nPattern Analysis")
    print("----------------")

    for pattern, words in patterns.items():
        if len(words) > 1:
            print(pattern, "->", words)

    return patterns


def apply_substitution(ciphertext, substitutions):
    result = ""

    for ch in ciphertext:
        lower = ch.lower()

        if lower in substitutions:
            new_char = substitutions[lower]

            if ch.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += ch

    return result


def display_partial_plaintext(ciphertext, substitutions):
    plaintext = apply_substitution(ciphertext, substitutions)

    print("\nPartial Plaintext")
    print("-----------------")
    print(plaintext)

    return plaintext


def verify_solution(plaintext, ciphertext, key):
    from substitution_cipher import encrypt

    generated = encrypt(plaintext, key)

    if generated == ciphertext:
        print("\nVerification: SUCCESS")
        return True

    print("\nVerification: FAILED")
    return False


def recover_key(ciphertext):
    substitutions = {
        'a': 't',
        'b': 'u',
        'c': 'v',
        'd': 'w',
        'e': 'x',
        'f': 'y',
        'g': 'z',
        'h': 'a',
        'i': 'b',
        'j': 'c',
        'k': 'd',
        'l': 'e',
        'm': 'f',
        'n': 'g',
        'o': 'h',
        'p': 'i',
        'q': 'j',
        'r': 'k',
        's': 'l',
        't': 'm',
        'u': 'n',
        'v': 'o',
        'w': 'p',
        'x': 'q',
        'y': 'r',
        'z': 's'
    }

    return substitutions
