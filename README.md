# public-key-signature-generator

ECDSA Signature Generation without Private Key
This repo demonstrates an interesting cryptographic technique for generating valid ECDSA signatures using only a public key. While these signatures verify correctly, they don't require knowledge of the private key - highlighting an important security consideration in ECDSA implementation.
The core concept relies on the mathematical properties of ECDSA:

Instead of using R = k*G (the standard approach with a private key nonce), we use:
R = u1*G + u2*Q where:

u1 and u2 are random values
G is the generator point
Q is the public key


We then calculate signature components:

r becomes the x-coordinate of R
s = r * inv(u2, N) % N
z = u1 * r * inv(u2, N) % N (this is the message hash)


The signature (r,s) will verify correctly against the public key Q and message hash z.

Usage Instructions

First, input your public key in decimal format:
python# Provide public key coordinates in decimal
X = 1234567890  # Replace with your public key X coordinate
Y = 0987654321  # Replace with your public key Y coordinate
Q = (X, Y)

Set the number of signatures to generate:
python# Number of signatures to generate
NUM_SIGS = 10  # Adjust as needed

Run the script:
python3 pubkey-gen.py

The output will show:

Your public key in hex format
Multiple valid signature sets (r, s, z)
Each signature can be verified against your public key

How It Works
This tool demonstrates how valid ECDSA signatures can be mathematically generated using only public key information. While these signatures verify correctly, they're created without using the private key.
