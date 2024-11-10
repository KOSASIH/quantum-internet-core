# src/qkd/bb84.py

import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BB84:
    def __init__(self):
        self.basis_choices = ['Z', 'X']  # Z basis (0, 1) and X basis (+, -)
        self.key_bits = []
        self.bases = []

    def generate_key_bits(self, num_bits=100):
        """Generate random key bits and their corresponding bases."""
        self.key_bits = []
        self.bases = []
        for _ in range(num_bits):
            bit = np.random.randint(0, 2)  # Random bit (0 or 1)
            basis = np.random.choice(self.basis_choices)  # Random basis
            self.key_bits.append(bit)
            self.bases.append(basis)
        logging.info(f"Generated key bits: {self.key_bits} with bases: {self.bases}")

    def measure(self, bit, basis):
        """Simulate measurement of a bit in a given basis."""
        if basis not in self.basis_choices:
            logging.error(f"Invalid basis: {basis}. Must be 'Z' or 'X'.")
            raise ValueError(f"Invalid basis: {basis}. Must be 'Z' or 'X'.")

        # Simulate measurement outcome
        if basis == 'Z':
            return bit  # Direct measurement
        else:
            # Random outcome for X basis (simulating the effect of measurement)
            return np.random.randint(0, 2)

    def sift_key(self, other_key_bits, other_bases):
        """Sift the key based on matching bases."""
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
