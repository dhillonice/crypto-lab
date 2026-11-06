
import random
import secrets
import string
import time


# ----------------------------------------
# Common MT19937 Stream Cipher Function
# ----------------------------------------

def cipher(data, seed):
    rng = random.Random(seed)
    result = bytearray()

    for byte in data:
        key = rng.getrandbits(8)
        result.append(byte ^ key)

    return bytes(result)


# ----------------------------------------
# PART A: MT19937 Stream Cipher
# ----------------------------------------

print("\n========== PART A ==========")

# Generate random printable prefix of 5-20 characters
prefix_length = secrets.randbelow(16) + 5

characters = string.ascii_letters + string.digits + string.punctuation + " "

prefix = ''.join(secrets.choice(characters)
                 for _ in range(prefix_length))

# Add 14 consecutive A characters
plaintext = (prefix + "A" * 14).encode("ascii")

# Generate a random 16-bit seed
original_seed = secrets.randbelow(65536)

# Encrypt the plaintext
ciphertext = cipher(plaintext, original_seed)

print("\nOriginal Plaintext:", plaintext.decode("ascii"))
print("Original Seed:", original_seed)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt using the original seed
decrypted = cipher(ciphertext, original_seed)

print("Decrypted Plaintext:", decrypted.decode("ascii"))
print("Encryption/Decryption Verified:", decrypted == plaintext)


# ----------------------------------------
# PART A: Brute Force Seed Recovery
# ----------------------------------------

print("\n----- SEED RECOVERY ATTACK -----")

recovered_seed = None
recovered_plaintext = None

for seed in range(65536):

    candidate_plaintext = cipher(ciphertext, seed)

    if b"A" * 14 in candidate_plaintext:
        recovered_seed = seed
        recovered_plaintext = candidate_plaintext
        break

print("Recovered Seed:", recovered_seed)

if recovered_seed is not None:

    print("Recovered Plaintext:",
          recovered_plaintext.decode("ascii"))

    position = recovered_plaintext.find(b"A" * 14)

    # Recover the known keystream segment
    known_keystream = bytes(
        ciphertext[i] ^ ord('A')
        for i in range(position, position + 14)
    )

    print("Position of Known Pattern:", position)
    print("Recovered Keystream Segment:", known_keystream.hex())

    # Verify the complete plaintext
    verification = cipher(ciphertext, recovered_seed)

    print("Full Plaintext Verification:",
          verification == plaintext)

    print("Known Pattern Verification:",
          b"A" * 14 in verification)

else:
    print("Seed not recovered!")


# ----------------------------------------
# PART B: Predictable Password Reset Token
# ----------------------------------------

print("\n========== PART B ==========")

def generate_token(seed):
    rng = random.Random(seed)

    token = bytes(rng.getrandbits(8) for _ in range(16))

    return token


# Record current Unix timestamp
timestamp = int(time.time())

# Generate token using timestamp as seed
observed_token = generate_token(timestamp)

print("\nOriginal Timestamp:", timestamp)
print("Observed Token:", observed_token.hex())


# ----------------------------------------
# PART B: Timestamp Prediction Attack
# ----------------------------------------

print("\n----- TIMESTAMP RECOVERY ATTACK -----")

start_time = timestamp - 300
end_time = timestamp + 300

print("Search Start:", start_time)
print("Search End:", end_time)

recovered_timestamp = None
candidates_tested = 0

# Test every possible timestamp
for candidate in range(start_time, end_time + 1):

    candidates_tested += 1

    candidate_token = generate_token(candidate)

    if candidate_token == observed_token:
        recovered_timestamp = candidate

print("Candidates Tested:", candidates_tested)
print("Recovered Timestamp:", recovered_timestamp)

# Verify recovered timestamp
if recovered_timestamp is not None:

    verification_token = generate_token(recovered_timestamp)

    print("Regenerated Token:", verification_token.hex())

    print("Token Verification:",
          verification_token == observed_token)

else:
    print("Timestamp not recovered!")

print("\n========== ASSIGNMENT COMPLETED ==========")
