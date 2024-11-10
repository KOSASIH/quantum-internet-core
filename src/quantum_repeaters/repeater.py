# src/quantum_repeaters/repeater.py

import uuid
import logging
from entanglement_swapping import EntanglementSwapping
from error_correction import ErrorCorrection
from quantum_state_visualization import QuantumStateVisualizer

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Repeater:
    def __init__(self, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.entangled_pairs = []
        self.entanglement_swapping = EntanglementSwapping()
        self.error_correction = ErrorCorrection()
        self.visualizer = QuantumStateVisualizer()
        self.is_running = False

    def start(self):
        """Start the repeater to manage entangled states."""
        self.is_running = True
        logging.info(f"Repeater {self.id} started.")

    def stop(self):
        """Stop the repeater."""
        self.is_running = False
        logging.info(f"Repeater {self.id} stopped.")

    def add_entangled_pair(self, pair):
        """Add an entangled pair to the repeater."""
        if self.is_running:
            self.entangled_pairs.append(pair)
            logging.info(f"Entangled pair {pair} added to repeater {self.id}.")
        else:
            logging.warning("Repeater is not running. Cannot add entangled pair.")

    def perform_entanglement_swapping(self):
        """Perform entanglement swapping on the stored pairs."""
        if self.is_running and len(self.entangled_pairs) >= 2:
            new_pair = self.entanglement_swapping.swap(self.entangled_pairs)
            self.entangled_pairs.append(new_pair)
            logging.info(f"Entanglement swapping performed. New pair: {new_pair}")
            self.visualize_entangled_pairs()
        else:
            logging.warning("Not enough entangled pairs or repeater is not running.")

    def correct_errors(self):
        """Apply error correction to the entangled pairs."""
        if self.is_running:
            for i, pair in enumerate(self.entangled_pairs):
                corrected_pair = self.error_correction.correct(pair)
                self.entangled_pairs[i] = corrected_pair
                logging.info(f"Corrected pair: {corrected_pair}")
        else:
            logging.warning("Repeater is not running. Cannot correct errors.")

    def visualize_entangled_pairs(self):
        """Visualize the current entangled pairs."""
        if self.is_running:
            self.visualizer.visualize(self.entangled_pairs)
        else:
            logging.warning("Repeater is not running. Cannot visualize entangled pairs.")

    def get_status(self):
        """Get the current status of the repeater."""
        status = {
            "id": self.id,
            "is_running": self.is_running,
            "entangled_pairs_count": len(self.entangled_pairs)
        }
        logging.info(f"Repeater status: {status}")
        return status

    def reset(self):
        """Reset the repeater, clearing all entangled pairs."""
        if self.is_running:
            self.entangled_pairs.clear()
            logging.info(f"Repeater {self.id} has been reset.")
        else:
            logging.warning("Repeater is not running. Cannot reset.")
