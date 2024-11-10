# simulations/quantum_simulator.py

import numpy as np
from scipy.linalg import expm
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumSimulator:
    def __init__(self, num_qubits):
        """Initialize the quantum simulator with a specified number of qubits."""
        self.num_qubits = num_qubits
        self.state = self.initialize_state()
        logging.info(f"Quantum simulator initialized with {num_qubits} qubits.")

    def initialize_state(self):
        """Initialize the quantum state to |0...0>."""
        return np.zeros((2 ** self.num_qubits, 1), dtype=complex)

    def apply_gate(self, gate, target_qubit):
        """Apply a quantum gate to a specific qubit in the state."""
        if target_qubit < 0 or target_qubit >= self.num_qubits:
            raise ValueError("Target qubit index out of range.")
        
        # Create the full gate for the specified qubit
        full_gate = np.eye(2 ** self.num_qubits, dtype=complex)
        full_gate = self._apply_single_gate(full_gate, gate, target_qubit)
        
        # Update the state
        self.state = np.dot(full_gate, self.state)
        logging.info(f"Applied gate {gate} to qubit {target_qubit}.")

    def _apply_single_gate(self, full_gate, gate, target_qubit):
        """Apply a single qubit gate to the full gate matrix."""
        gate_size = gate.shape[0]
        for i in range(2 ** self.num_qubits):
            if (i >> target_qubit) & 1:
                full_gate[i, i] = gate[1, 1]
                if gate_size > 1:
                    full_gate[i, i ^ (1 << target_qubit)] = gate[1, 0]
            else:
                full_gate[i, i] = gate[0, 0]
                if gate_size > 1:
                    full_gate[i, i ^ (1 << target_qubit)] = gate[0, 1]
        return full_gate

    def measure(self):
        """Perform a measurement on the quantum state."""
        probabilities = np.abs(self.state) ** 2
        outcome = np.random.choice(range(2 ** self.num_qubits), p=probabilities.flatten())
        logging.info(f"Measurement outcome: {outcome}")
        return outcome

    def get_state(self):
        """Return the current quantum state."""
        return self.state
