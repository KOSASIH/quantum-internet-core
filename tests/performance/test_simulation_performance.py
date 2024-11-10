# performance/test_simulation_performance.py

import unittest
import time
import tracemalloc
from quantum_simulator import QuantumSimulator  # Assuming this is the module for the quantum simulator

class TestSimulationPerformance(unittest.TestCase):
    def setUp(self):
        """Set up a QuantumSimulator instance for performance testing."""
        self.simulator = QuantumSimulator(num_qubits=10)

    def test_simulation_execution_time(self):
        """Test the execution time of a series of quantum gate applications."""
        gates = [self.simulator.apply_gate(np.array([[1, 0], [0, 1]]), 0),  # Identity gate
                 self.simulator.apply_gate(np.array([[0, 1], [1, 0]]), 1)]  # Pauli-X gate

        start_time = time.time()
        for gate in gates:
            self.simulator.apply_gate(gate, 0)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Quantum gate application execution time: {execution_time:.4f} seconds")
        self.assertLess(execution_time, 0.5)  # Assuming we want it to be under 0.5 seconds

    def test_simulation_memory_usage(self):
        """Test the memory usage during a simulation run."""
        tracemalloc.start()
        for _ in range(1000):  # Simulate multiple gate applications
            self.simulator.apply_gate(np.array([[0, 1], [1, 0]]), 0)  # Pauli-X gate
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current memory usage: {current / 10**6:.4f} MB; Peak: {peak / 10**6:.4f} MB")
        self.assertLess(peak, 100 * 10**6)  # Assuming we want peak memory usage under 100 MB

if __name__ == '__main__':
    unittest.main()
