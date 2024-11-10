# src/qkd/e91.py

import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class E91:
    def __init__(self):
        self.key_bits = []
        self.bases = []

    def generate_key_bits(self, num_bits=100):
        """Generate key bits based on entangled photon pairs."""
        self.key_bits = []
        self.bases = []
        for _ in range(num_bits):
            bit = np.random.randint(0, 2)  # Random bit (0 or 1)
            basis = np.random.choice(['A', 'B'])  # Random basis (A or B)
            self.key_bits.append(bit)
            self.bases.append(basis)
        logging.info(f"Generated key bits: {self.key_bits} with bases: {self.bases}")

    def measure(self, bit, basis):
        """Simulate measurement of a quantum state in a given basis."""
        if basis not in ['A', 'B']:
            logging.error(f"Invalid basis: {basis}. Must be 'A' or 'B'.")
            raise ValueError(f"Invalid basis: {basis}. Must be 'A' or 'B'.")

        # Simulate measurement outcome based on the basis
        if basis == 'A':
            return bit  # Direct measurement for basis A
        else:
            # Inverse measurement for basis B (simulating the effect of measurement)
            return 1 - bit

    def sift_key(self, other_key_bits, other_bases):
        """Sift the key based on matching measurement outcomes."""
        sifted_key = []
        for (bit, basis), (other_bit, other_basis) in zip(zip(self.key_bits, self.bases), zip(other_key_bits, other_bases)):
            if basis == other_basis:
                sifted_key.append(bit)
        logging.info(f"Sifted key: {sifted_key}")
        return sifted_key

    def get_key(self):
        """Return the generated key bits."""
        return self.key_bits

    def get_bases(self):
        """Return the bases used for the generated key bits."""
        return self.bases
