# performance/test_performance_metrics.py

import unittest
import time
import tracemalloc
from quantum_repeaters import QuantumRepeater  # Assuming this is the module for quantum repeaters

class TestPerformanceMetrics(unittest.TestCase):
    def setUp(self):
        """Set up a QuantumRepeater instance for performance testing."""
        self.repeater = QuantumRepeater(num_nodes=100)

    def test_execution_time(self):
        """Test the execution time of entanglement distribution."""
        start_time = time.time()
        self.repeater.distribute_entanglement()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Entanglement distribution execution time: {execution_time:.4f} seconds")
        self.assertLess(execution_time, 1.0)  # Assuming we want it to be under 1 second

    def test_memory_usage(self):
        """Test the memory usage during entanglement distribution."""
        tracemalloc.start()
        self.repeater.distribute_entanglement()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current memory usage: {current / 10**6:.4f} MB; Peak: {peak / 10**6:.4f} MB")
        self.assertLess(peak, 50 * 10**6)  # Assuming we want peak memory usage under 50 MB

if __name__ == '__main__':
    unittest.main()
