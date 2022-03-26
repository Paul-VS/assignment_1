## Generates prime numbers with the Lucas-Lehmer primality test
## Encrypts and decrypts a user defined message using asymmetric encryption keys

import random

# Lucas Lehmer test for prime Mersenne numbers
# Given the value p, returns true if a Mersenne number Mₚ = 2ᵖ - 1 is prime
def lucas_lehmer(p):
    s = 4
    M = 2 ** p - 1
    for x in range(p-2):
        s = (s * s - 2) % M
    return s == 0           

# Creates a public and private key from two randomly generated prime numbers
def generate_keys():
    primes = []
    while len(primes) < 2:
        x = random.randint(10, 610)
        if lucas_lehmer(x):
            primes.append(2 ** x - 1)
    p, q, e = primes[0], primes[1], 3
    n, d = p*q, (e**-1)%((p-1)*(q-1))
    return (n,e),(n,d)

# Encrypts a message with a given public key
def encrypt(message, public_key):
    c = []
    for char in message:
        c.append(str(ord(char) ** public_key[1] % public_key[0]).zfill(8))
    return ''.join(c)

# Decrypts a message with a given private key
def decrypt(encrypted_message, private_key):
    c = [encrypted_message[i:i+8] for i in range(0, len(encrypted_message), 8)]
    message = [chr(int(round(int(x) ** private_key[1] % private_key[0]))) for x in c]
    return ''.join(message)

public_key, private_key = generate_keys()
message = input("Message to encrypt: ")
encrypted_message = encrypt(message, public_key)
print("Encrypted Message: " + encrypted_message)
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message: " + decrypted_message)




