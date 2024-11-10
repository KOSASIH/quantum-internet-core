# simulations/quantum_experiment.py

import logging
from quantum_circuit import QuantumCircuit
from analysis_tools import AnalysisTools

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumExperiment:
    def __init__(self, num_qubits, noise_level):
        """Initialize the quantum experiment with a specified number of qubits and noise level."""
        self.circuit = QuantumCircuit(num_qubits)
        self.circuit.noise_model.set_noise_level(noise_level)
        logging.info(f"Quantum experiment initialized with {num_qubits} qubits and noise level: {noise_level}")

    def run_experiment(self, gates, num_measurements):
        """Run the quantum experiment with specified gates and number of measurements."""
        for gate, target_qubit in gates:
            self.circuit.add_gate(gate, target_qubit)
        
        results = []
        for _ in range(num_measurements):
            self.circuit.apply_noise()
            result = self.circuit.measure()
            results.append(result)

        self.analyze_results(results)

    def analyze_results(self, results):
        """Analyze the results of the measurements."""
        probabilities = np.bincount(results) / len(results)
        AnalysisTools.plot_probabilities(probabilities)
