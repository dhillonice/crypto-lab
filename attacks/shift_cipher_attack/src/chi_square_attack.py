ENGLISH_FREQUENCIES = [
    8.167,  # A
    1.492,  # B
    2.782,  # C
    4.253,  # D
    12.702, # E
    2.228,  # F
    2.015,  # G
    6.094,  # H
    6.966,  # I
    0.153,  # J
    0.772,  # K
    4.025,  # L
    2.406,  # M
    6.749,  # N
    7.507,  # O
    1.929,  # P
    0.095,  # Q
    5.987,  # R
    6.327,  # S
    9.056,  # T
    2.758,  # U
    0.978,  # V
    2.360,  # W
    0.150,  # X
    1.974,  # Y
    0.074   # Z
]


def calculate_chi_square(text):

    text = text.upper()

    letters = []

    for char in text:
        if char.isalpha():
            letters.append(char)

    n = len(letters)

    if n == 0:
        return float("inf")

    observed = [0] * 26

    for char in letters:
        observed[ord(char) - ord('A')] += 1

    chi_square = 0

    for i in range(26):

        expected = ENGLISH_FREQUENCIES[i] * n / 100

        if expected != 0:

            chi_square += (
                (observed[i] - expected) ** 2
                / expected
            )

    return chi_square


def chi_square_attack(ciphertext, decrypt_function):

    best_key = None
    best_plaintext = ""
    lowest_chi_square = float("inf")

    results = []

    for key in range(26):

        plaintext = decrypt_function(ciphertext, key)

        score = calculate_chi_square(plaintext)

        results.append({
            "key": key,
            "plaintext": plaintext,
            "chi_square": score
        })

        if score < lowest_chi_square:

            lowest_chi_square = score
            best_key = key
            best_plaintext = plaintext

    return (
        best_key,
        best_plaintext,
        lowest_chi_square,
        results
    )