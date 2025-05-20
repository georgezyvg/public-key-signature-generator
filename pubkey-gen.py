# -*- coding: utf-8 -*-

from bitcoin import fast_add, fast_multiply, G, inv, N
from random import SystemRandom

# Provide public key coordinates in decimal
X = 5831721406635063654683117253506846208566679410118154188144422804291796683505
Y = 61770026510604113021686089777374557608174938587526483912023179154647723408296
Q = (X, Y)

# Number of signatures to generate
NUM_SIGS = 10

def generate_signatures():
    """Generate and validate ECDSA signatures."""
    print("ECDSA Signature")
    print("=" * 70)
    print(f"Using public key:")
    print(f"Qx: 0x{X:064x}")
    print(f"Qy: 0x{Y:064x}")
    print("-" * 70)
    
    for i in range(NUM_SIGS):
        # Generaterandom scalars
        u1 = SystemRandom().randrange(1, N)
        u2 = SystemRandom().randrange(1, N)

        # Calculate signature components
        R = fast_add(fast_multiply(G, u1), fast_multiply(Q, u2))
        r = R[0]
        s = r * inv(u2, N) % N
        z = u1 * r * inv(u2, N) % N

        # Verify the signature
        w = inv(s, N)
        v1 = z * w % N
        v2 = r * w % N
        verification_point = fast_add(fast_multiply(G, v1), fast_multiply(Q, v2))
        assert r == verification_point[0], "Signature verification failed"

        # Print
        print(f"\nSignature {i+1}/{NUM_SIGS}:")
        print(f"r: 0x{r:064x}")
        print(f"s: 0x{s:064x}")
        print(f"z: 0x{z:064x}")
        print("-" * 70)
    
    print("\nSignature generation completed successfully.")

if __name__ == "__main__":
    generate_signatures()
