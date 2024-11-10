# simulations/noise_model.py

import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NoiseModel:
    def __init__(self, noise_level=0.1):
        """Initialize the noise model with a specified noise level."""
        self.noise_level = noise_level
        logging.info(f"Noise model initialized with noise level: {noise_level}")

    def apply_noise(self, state):
        """Apply noise to a quantum state."""
        noise_matrix = self._generate_noise_matrix()
        noisy_state = np.dot(noise_matrix, state)
        logging.info("Noise applied to the quantum state.")
        return noisy_state

    def _generate_noise_matrix(self):
        """Generate a noise matrix based on the specified noise level."""
        identity = np.eye(2)
        noise = np.array([[1 - self.noise_level, 0],
                          [0, self.noise_level]])
        return np.kron(identity, noise)

    def set_noise_level(self, new_noise_level):
        """Set a new noise level."""
        self.noise_level = new_noise_level
        logging.info(f"Noise level updated to: {new_noise_level}")
