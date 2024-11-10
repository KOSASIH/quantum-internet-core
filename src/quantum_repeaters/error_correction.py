# src/quantum_repeaters/error_correction.py

import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ErrorCorrection:
    def __init__(self):
        self.error_correction_code = "Shor"  # Default error correction code

    def correct(self, pair):
        """Apply error correction to an entangled pair."""
        logging.info(f"Applying error correction to pair: {pair}")
        
        # Simulate the error detection process
        if self._detect_errors(pair):
            corrected_pair = self._apply_correction(pair)
            logging.info(f"Errors detected and corrected. Original pair: {pair}, Corrected pair: {corrected_pair}")
            return corrected_pair
        else:
            logging.info("No errors detected in the pair.")
            return pair  # No correction needed

    def _detect_errors(self, pair):
        """Simulate error detection in a quantum pair."""
        # For demonstration, we randomly decide if an error is detected
        error_detected = np.random.choice([True, False], p=[0.2, 0.8])  # 20% chance of error
        if error_detected:
            logging.warning(f"Error detected in pair: {pair}")
        return error_detected

    def _apply_correction(self, pair):
        """Apply the chosen error correction code to the pair."""
        if self.error_correction_code == "Shor":
            return self._shor_correction(pair)
        elif self.error_correction_code == "Steane":
            return self._steane_correction(pair)
        else:
            logging.error(f"Unknown error correction code: {self.error_correction_code}")
            raise ValueError(f"Unknown error correction code: {self.error_correction_code}")

    def _shor_correction(self, pair):
        """Apply Shor's error correction code."""
        # Simulate Shor's error correction logic
        corrected_pair = (self._correct_qubit(pair[0]), self._correct_qubit(pair[1]))
        return corrected_pair

    def _steane_correction(self, pair):
        """Apply Steane's error correction code."""
        # Simulate Steane's error correction logic
        corrected_pair = (self._correct_qubit(pair[0]), self._correct_qubit(pair[1]))
        return corrected_pair

    def _correct_qubit(self, qubit):
        """Simulate the correction of a single qubit."""
        # For demonstration, we simply return a modified version of the qubit
        corrected_qubit = f"corrected({qubit})"
        return corrected_qubit

    def set_error_correction_code(self, code):
        """Set the error correction code to be used."""
        valid_codes = ["Shor", "Steane"]
        if code in valid_codes:
            self.error_correction_code = code
            logging.info(f"Error correction code set to: {self.error_correction_code}")
        else:
            logging.error(f"Invalid error correction code: {code}. Valid options are: {valid_codes}")
            raise ValueError(f"Invalid error correction code: {code}. Valid options are: {valid_codes}")
