# src/entanglement/entanglement_manager.py

import logging
from entangler import Entangler
from measurement import Measurement

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EntanglementManager:
    def __init__(self):
        self.entangler = Entangler()
        self.measurement = Measurement()

    def create_entangled_pair(self, state_type='bell'):
        """Create a new entangled pair of the specified type."""
        try:
            return self.entangler.generate_entangled_pair(state_type)
        except ValueError as e:
            logging.error(f"Failed to create entangled pair: {e}")
            return None

    def measure_pair(self, pair, basis='standard'):
        """Measure an entangled pair and return the outcome."""
        try:
            return self.measurement.perform_correlation_measurement(pair, basis)
        except ValueError as e:
            logging.error(f"Failed to measure pair: {e}")
            return None

    def list_entangled_pairs(self):
        """List all generated entangled pairs."""
        pairs = self.entangler.get_entangled_pairs()
        if pairs:
            logging.info(f"Current entangled pairs: {pairs}")
        else:
            logging.info("No entangled pairs available.")
        return pairs

    def clear_entangled_pairs(self):
        """Clear all entangled pairs."""
        self.entangler.clear_entangled_pairs()

    def simulate_noise_on_pair(self, pair, noise_level=0.1):
        """Simulate noise affecting the entangled pair."""
        try:
            noisy_pair = self.entangler.simulate_noise(pair, noise_level)
            logging.info(f"Noisy pair: {noisy_pair}")
            return noisy_pair
        except ValueError as e:
            logging.error(f"Failed to simulate noise on pair: {e}")
            return None

    def calculate_fidelity(self, pair, ideal_state):
        """Calculate the fidelity of the entangled pair with respect to an ideal state."""
        try:
            fidelity = self.entangler.entanglement_fidelity(pair, ideal_state)
            logging.info(f"Fidelity of the pair: {fidelity}")
            return fidelity
        except Exception as e:
            logging.error(f"Failed to calculate fidelity: {e}")
            return None

    def visualize_entangled_pairs(self):
        """Visualize the entangled pairs (placeholder for actual visualization logic)."""
        self.entangler.visualize_entangled_pairs()

    def visualize_measurement_results(self, results):
        """Visualize the measurement results."""
        self.measurement.visualize_measurement_results(results)
