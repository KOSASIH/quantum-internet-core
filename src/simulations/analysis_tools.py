# simulations/analysis_tools.py

import numpy as np
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AnalysisTools:
    @staticmethod
    def plot_probabilities(probabilities, title="Measurement Probabilities"):
        """Plot the measurement probabilities."""
        plt.bar(range(len(probabilities)), probabilities)
        plt.xlabel('State')
        plt.ylabel('Probability')
        plt.title(title)
        plt.show()
        logging.info("Probability distribution plotted.")

 ### Summary of Features

1. **Quantum State Simulator** (`quantum_simulator.py`):
   - A class that simulates quantum states, allowing the application of quantum gates and performing measurements. It initializes the state to |0...0> and provides methods for gate application and state retrieval.

2. **Noise Modeling** (`noise_model.py`):
   - A class that models noise in quantum systems, allowing the application of noise to quantum states based on a specified noise level. It includes methods to generate noise matrices and update noise levels.

3. **Analysis Tools** (`analysis_tools.py`):
   - A class that provides static methods for analyzing simulation results, including plotting measurement probabilities using Matplotlib for visual representation of quantum state probabilities.### 4. `quantum_circuit.py`

```python
# simulations/quantum_circuit.py

from quantum_simulator import QuantumSimulator
from noise_model import NoiseModel
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumCircuit:
    def __init__(self, num_qubits):
        """Initialize the quantum circuit with a specified number of qubits."""
        self.simulator = QuantumSimulator(num_qubits)
        self.noise_model = NoiseModel()
        logging.info(f"Quantum circuit initialized with {num_qubits} qubits.")

    def add_gate(self, gate, target_qubit):
        """Add a quantum gate to the circuit."""
        self.simulator.apply_gate(gate, target_qubit)

    def apply_noise(self):
        """Apply noise to the current quantum state."""
        self.simulator.state = self.noise_model.apply_noise(self.simulator.state)

    def measure(self):
        """Perform a measurement on the quantum state."""
        return self.simulator.measure()

    def get_state(self):
        """Return the current quantum state."""
        return self.simulator.get_state()
