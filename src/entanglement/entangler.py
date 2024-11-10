# src/entanglement/entangler.py

import logging
import numpy as np
from scipy.linalg import sqrtm

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Entangler:
    def __init__(self):
        self.entangled_pairs = []

    def generate_entangled_pair(self, state_type='bell'):
        """Generate a new entangled pair of the specified type."""
        if state_type not in ['bell', 'ghz', 'w']:
            logging.error(f"Invalid state type: {state_type}. Must be 'bell', 'ghz', or 'w'.")
            raise ValueError(f"Invalid state type: {state_type}. Must be 'bell', 'ghz', or 'w'.")

        if state_type == 'bell':
            pair = self._create_bell_state()
        elif state_type == 'ghz':
            pair = self._create_ghz_state()
        elif state_type == 'w':
            pair = self._create_w_state()

        self.entangled_pairs.append(pair)
        logging.info(f"Generated new entangled pair of type '{state_type}': {pair}")
        return pair

    def _create_bell_state(self):
        """Create a Bell state (|Φ+⟩ = (|00⟩ + |11⟩) / √2)."""
        return (np.array([1, 0, 0, 1]) / np.sqrt(2)).tolist()  # Representing |Φ+⟩

    def _create_ghz_state(self):
        """Create a GHZ state (|GHZ⟩ = (|000⟩ + |111⟩) / √2)."""
        return (np.array([1, 0, 0, 0, 0, 0, 0, 1]) / np.sqrt(2)).tolist()  # Representing |GHZ⟩

    def _create_w_state(self):
        """Create a W state (|W⟩ = (|001⟩ + |010⟩ + |100⟩) / √3)."""
        return (np.array([1, 0, 1, 0, 1, 0]) / np.sqrt(3)).tolist()  # Representing |W⟩

    def get_entangled_pairs(self):
        """Return the list of currently generated entangled pairs."""
        return self.entangled_pairs

    def clear_entangled_pairs(self):
        """Clear the list of entangled pairs."""
        self.entangled_pairs.clear()
        logging.info("Cleared all entangled pairs.")

    def simulate_noise(self, pair, noise_level=0.1):
        """Simulate noise affecting the entangled pair."""
        if not (0 <= noise_level <= 1):
            logging.error("Noise level must be between 0 and 1.")
            raise ValueError("Noise level must be between 0 and 1.")

        noise_matrix = np.array([[1 - noise_level, noise_level],
                                  [noise_level, 1 - noise_level]])
        noisy_pair = np.dot(noise_matrix, pair)
        logging.info(f"Applied noise to pair: {pair} -> {noisy_pair}")
        return noisy_pair

    def entanglement_fidelity(self, pair, ideal_state):
        """Calculate the fidelity of the entangled pair with respect to an ideal state."""
        fidelity = np.abs(np.dot(np.conj(pair), ideal_state)) ** 2
        logging.info(f"Calculated fidelity: {fidelity}")
        return fidelity

    def visualize_entangled_pairs(self):
        """Visualize the entangled pairs (placeholder for actual visualization logic)."""
        logging.info("Visualizing entangled pairs...")
        for i, pair in enumerate(self.entangled_pairs):
            logging.info(f"Pair {i}: {pair}")
