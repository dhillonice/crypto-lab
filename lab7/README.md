# Padding Oracle Attack

## Lab 7 | CryptoLabX Group 15 | 22CPP307

### Objective
Demonstrate how a padding oracle attack can recover plaintext
from an AES-CBC encrypted message without knowing the AES key.

## Tasks
1. Understand AES-CBC and PKCS#7 padding.
2. Implement plaintext recovery using a padding oracle.
3. Record the number of oracle queries.
4. Explain how to prevent padding oracle vulnerabilities.

## Folder Structure

- `src/` - Python implementation
- `data/` - Input ciphertext and IV
- `outputs/` - Recovered plaintext and query statistics
- `reports/` - Assignment report
- `screenshots/` - Execution screenshots

## Security Note
The AES key is used only by the encryption and oracle simulation.
The attack implementation must not access the key directly.
