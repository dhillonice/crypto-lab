import re


def load_dictionary(filename):
    with open(filename, "r") as file:
        words = set()

        for line in file:
            word = line.strip().lower()

            if word:
                words.add(word)

    return words


def score_text(text, dictionary):
    words = re.findall(r"[a-zA-Z]+", text.lower())

    score = 0

    for word in words:
        if word in dictionary:
            score += 1

    return score


def brute_force_dictionary(ciphertext, decrypt_function, dictionary):

    best_key = None
    best_plaintext = ""
    best_score = -1

    results = []

    for key in range(26):

        plaintext = decrypt_function(ciphertext, key)

        score = score_text(plaintext, dictionary)

        results.append({
            "key": key,
            "plaintext": plaintext,
            "score": score
        })

        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext, best_score, results