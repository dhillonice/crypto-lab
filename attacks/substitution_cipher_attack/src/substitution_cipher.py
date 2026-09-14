import string

def generate_key():
    alphabet = string.ascii_lowercase
    key = list(alphabet)
    
    shift = 7
    key = key[shift:] + key[:shift]
    
    return dict(zip(alphabet, key))

def encrypt(plaintext, key):
    ciphertext = ""

    for ch in plaintext:
        if ch.lower() in key:
            encrypted = key[ch.lower()]
            ciphertext += encrypted.upper() if ch.isupper() else encrypted
        else:
            ciphertext += ch

    return ciphertext

def decrypt(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}
    plaintext = ""

    for ch in ciphertext:
        if ch.lower() in reverse_key:
            decrypted = reverse_key[ch.lower()]
            plaintext += decrypted.upper() if ch.isupper() else decrypted
        else:
            plaintext += ch

    return plaintext
