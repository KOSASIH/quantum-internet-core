# tests/unit/test_quantum_repeaters.py

import unittest
from quantum_repeaters import QuantumRepeater  # Assuming this is the module for quantum repeaters

class TestQuantumRepeaters(unittest.TestCase):
    def setUp(self):
        """Set up a QuantumRepeater instance for testing."""
        self.repeater = QuantumRepeater(num_nodes=5)

    def test_initialization(self):
        """Test the initialization of the quantum repeater."""
        self.assertEqual(self.repeater.num_nodes, 5)
        self.assertEqual(len(self.repeater.nodes), 5)

    def test_entanglement_distribution(self):
        """Test the entanglement distribution between nodes."""
        self.repeater.distribute_entanglement()
        for node in self.repeater.nodes:
            self.assertTrue(node.is_entangled)

    def test_repeater_functionality(self):
        """Test the functionality of the repeater."""
        result = self.repeater.transmit_message("Hello, Quantum World!")
        self.assertEqual(result, "Message transmitted successfully.")

if __name__ == '__main__':
    unittest.main()
