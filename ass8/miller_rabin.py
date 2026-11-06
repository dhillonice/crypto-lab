
import secrets
import time
from sympy import isprime

BITS = 512
ROUNDS = 20


def miller_rabin(n, rounds):
    if n < 2:
        return False, []

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    for p in small_primes:
        if n == p:
            return True, []
        if n % p == 0:
            return False, []

    # Write n - 1 as 2^s * d
    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    bases = []

    # Perform Miller-Rabin rounds
    for i in range(rounds):
        a = secrets.randbelow(n - 3) + 2
        bases.append(a)

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for j in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False, bases

    return True, bases


def generate_prime(bits, rounds):
    count = 0

    while True:
        # Generate a random number of required bit length
        n = secrets.randbits(bits)

        # Set MSB and LSB to 1
        n = n | (1 << (bits - 1)) | 1

        count += 1

        is_prime, bases = miller_rabin(n, rounds)

        if is_prime:
            return n, count, bases


def main():
    print("MILLER-RABIN PRIME GENERATION")
    print("-" * 50)

    start = time.time()

    prime, count, bases = generate_prime(BITS, ROUNDS)

    end = time.time()

    print("\nGenerated probable prime:")
    print(prime)

    print("\nExperimental Results")
    print("-" * 50)
    print("Assigned bit length:", BITS)
    print("Actual bit length:", prime.bit_length())
    print("Number of candidates tested:", count)
    print("Miller-Rabin rounds:", ROUNDS)
    print("Execution time:", round(end - start, 4), "seconds")

    print("\nBases used for final candidate:")
    for i, a in enumerate(bases, 1):
        print("Round", i, ":", a)

    print("\nIndependent Verification")
    print("-" * 50)

    print("Correct bit length:",
          prime.bit_length() == BITS)

    print("Odd number:", prime % 2 == 1)

    print("SymPy verification:", isprime(prime))


if __name__ == "__main__":
    main()
