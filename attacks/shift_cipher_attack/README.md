# Shift Cipher Cryptanalysis

## Purpose

This project demonstrates cryptanalysis of the Shift Cipher using brute force with two different scoring methods:

1. Dictionary Scoring
2. Chi-Square Analysis

## Project Structure

```lab4
shift_cipher_attack/
├── src/
│   ├── shift_cipher.py
│   ├── brute_force_dictionary.py
│   ├── chi_square_attack.py
│   └── main.py
├── dictionary/
│   └── english_words.txt
├── testcases/
├── outputs/
├── screenshots/
├── reports/
└── README.md
```

## Shift Cipher

The Shift Cipher encrypts alphabetic characters by shifting them by a fixed key between 0 and 25.

## Dictionary Scoring Attack

The program tries all 26 possible keys.

For every possible key, the ciphertext is decrypted and the resulting plaintext is checked against an English dictionary.

The key producing the highest number of dictionary words is selected as the predicted key.

## Chi-Square Attack

The program tries all 26 possible keys.

For every possible plaintext, the Chi-Square statistic is calculated by comparing the observed letter frequencies with expected English letter frequencies.

The key with the lowest Chi-Square value is selected.

## How to Run

Navigate to the src directory:

```bash
cd src
```

Run:

```bash
python3 main.py
```

Enter a plaintext and encryption key when prompted.

## Experimental Results

| Test Case                                       | Actual Key | Dictionary Key | Chi-Square Key | Dictionary Correct | Chi-Square Correct |
| ----------------------------------------------- | ---------: | -------------: | -------------: | ------------------ | ------------------ |
| this is a secret message                        |          3 |              3 |              3 | True               | True               |
| hello world this is a test                      |          7 |              7 |              7 | True               | True               |
| cryptography is important for computer security |         15 |             15 |             15 | True               | True               |
| hello                                           |          5 |              5 |             16 | True               | False              |

## Observation

Dictionary scoring correctly predicted the key for all four test cases.

Chi-Square analysis correctly predicted the key for the three longer test cases but failed for the short plaintext "hello".

This demonstrates that Chi-Square frequency analysis is less reliable when the ciphertext contains only a small number of characters.

## Conclusion

The Shift Cipher is vulnerable to brute-force cryptanalysis because it has only 26 possible keys.

Dictionary scoring and Chi-Square analysis can both be used to identify the correct plaintext and encryption key. Dictionary scoring depends on the quality of the dictionary, while Chi-Square analysis depends on having sufficient ciphertext length for reliable frequency analysis.
