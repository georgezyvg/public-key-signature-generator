# Public Key Signature Generator

Generate valid ECDSA signatures using only public key information.

## Overview

This tool demonstrates an important cryptographic property of ECDSA: it's possible to generate valid signature pairs that will verify against a public key, without possessing the corresponding private key.

## Security Implications

This technique highlights a critical consideration in cryptographic implementations:
- Valid ECDSA signature verification alone doesn't prove private key possession
- Protocols should implement additional security measures
- This demonstrates why deterministic signatures (RFC 6979) are important

## Mathematical Approach

The implementation uses these cryptographic principles:

1. Standard ECDSA signature verification checks if: `R = z*G*w + r*Q*w`
2. This implementation reverses the process by:
   - Choosing random values `u1` and `u2`
   - Computing `R = u1*G + u2*Q`
   - Deriving `s` and `z` values that satisfy the verification equation

## Usage

1. Input your public key in decimal format:
   ```python
   # Provide public key coordinates in decimal
   X = 1234567890  # Replace with your public key X coordinate
   Y = 0987654321  # Replace with your public key Y coordinate
   ```

2. Set your desired number of signatures:
   ```python
   NUM_SIGS = 10  # Adjust as needed
   ```

3. Run the script:
   ```
   python3 pubkey-gen.py
   ```

4. The tool will generate multiple valid signature sets (r, s, z)

## Requirements

- Python 3.x
- Bitcoin library (`pip install bitcoin`)

## Educational Purpose

This tool is for educational purposes to better understand ECDSA properties. Production systems should implement proper signature validation beyond basic ECDSA verification.
