# src/quantum_repeaters/repeater_manager.py

import logging
from repeater import Repeater

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RepeaterManager:
    def __init__(self):
        self.repeaters = {}

    def add_repeater(self, repeater_id=None):
        """Add a new repeater to the manager."""
        repeater = Repeater(id=repeater_id)
        repeater.start()  # Start the repeater upon creation
        self.repeaters[repeater.id] = repeater
        logging.info(f"Repeater {repeater.id} added and started.")

    def remove_repeater(self, repeater_id):
        """Remove a repeater from the manager."""
        if repeater_id in self.repeaters:
            repeater = self.repeaters[repeater_id]
            repeater.stop()  # Stop the repeater before removal
            del self.repeaters[repeater_id]
            logging.info(f"Repeater {repeater_id} removed.")
        else:
            logging.warning(f"Repeater {repeater_id} not found.")

    def get_repeater(self, repeater_id):
        """Get a specific repeater by its ID."""
        return self.repeaters.get(repeater_id, None)

    def list_repeaters(self):
        """List all repeaters managed by the manager."""
        if not self.repeaters:
            logging.info("No repeaters currently managed.")
            return []
        logging.info(f"Managed repeaters: {list(self.repeaters.keys())}")
        return list(self.repeaters.keys())

    def perform_entanglement_swapping(self, repeater_id):
        """Perform entanglement swapping on a specific repeater."""
        repeater = self.get_repeater(repeater_id)
        if repeater:
            repeater.perform_entanglement_swapping()
        else:
            logging.warning(f"Repeater {repeater_id} not found.")

    def correct_errors(self, repeater_id):
        """Apply error correction on a specific repeater."""
        repeater = self.get_repeater(repeater_id)
        if repeater:
            repeater.correct_errors()
        else:
            logging.warning(f"Repeater {repeater_id} not found.")

    def visualize_entangled_pairs(self, repeater_id):
        """Visualize the entangled pairs of a specific repeater."""
        repeater = self.get_repeater(repeater_id)
        if repeater:
            repeater.visualize_entangled_pairs()
        else:
            logging.warning(f"Repeater {repeater_id} not found.")

    def get_repeater_status(self, repeater_id):
        """Get the status of a specific repeater."""
        repeater = self.get_repeater(repeater_id)
        if repeater:
            return repeater.get_status()
        else:
            logging.warning(f"Repeater {repeater_id} not found.")
            return None

    def reset_repeater(self, repeater_id):
        """Reset a specific repeater."""
        repeater = self.get_repeater(repeater_id)
        if repeater:
            repeater.reset()
        else:
            logging.warning(f"Repeater {repeater_id} not found.")
