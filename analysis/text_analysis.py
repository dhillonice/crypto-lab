from collections import Counter


def analyze_file(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()

        characters = len(text)
        words = len(text.split())
        lines = len(text.splitlines())
        unique_characters = len(set(text))

        letters = [ch.lower() for ch in text if ch.isalpha()]
        frequency = Counter(letters)

        print("\n========== Text Analysis ==========")
        print(f"Characters        : {characters}")
        print(f"Words             : {words}")
        print(f"Lines             : {lines}")
        print(f"Unique Characters : {unique_characters}")

        print("\nLetter Frequency")
        print("------------------------")

        for letter in sorted(frequency):
            print(f"{letter} : {frequency[letter]}")

    except FileNotFoundError:
        print("File not found!")