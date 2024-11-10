# src/qkd/qkd_manager.py

import logging
from bb84 import BB84
from e91 import E91

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QKDManager:
    def __init__(self, protocol='bb84'):
        """Initialize the QKD Manager with the specified protocol."""
        if protocol == 'bb84':
            self.qkd_protocol = BB84()
        elif protocol == 'e91':
            self.qkd_protocol = E91()
        else:
            logging.error(f"Invalid protocol: {protocol}. Must be 'bb84' or 'e91'.")
            raise ValueError(f"Invalid protocol: {protocol}. Must be 'bb84' or 'e91'.")

    def generate_key(self, num_bits=100):
        """Generate a key using the selected QKD protocol."""
        logging.info(f"Generating key using {self.qkd_protocol.__class__.__name__} protocol.")
        self.qkd_protocol.generate_key_bits(num_bits)

    def measure_key(self, bit, basis):
        """Measure a key bit in the specified basis."""
        logging.info(f"Measuring bit: {bit} in basis: {basis}.")
        return self.qkd_protocol.measure(bit, basis)

    def sift_key(self, other_key_bits, other_bases):
        """Sift the key based on the other party's key bits and bases."""
        logging.info("Sifting keys based on matching bases.")
        return self.qkd_protocol.sift_key(other_key_bits, other_bases)

    def get_key(self):
        """Retrieve the generated key."""
        return self.qkd_protocol.get_key()

    def get_bases(self):
        """Retrieve the bases used for the generated key bits."""
        return self.qkd_protocol.get_bases()
