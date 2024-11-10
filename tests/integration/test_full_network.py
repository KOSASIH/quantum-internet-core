# tests/integration/test_full_network.py

import unittest
from network import QuantumNetwork  # Assuming this is the module for the quantum network
from qkd import QKDProtocol  # Assuming this is the module for QKD protocols
from entanglement import EntanglementGenerator  # Assuming this is the module for entanglement generation

class TestFullNetworkIntegration(unittest.TestCase):
    def setUp(self):
        """Set up a full quantum network for integration testing."""
        self.network = QuantumNetwork()
        self.qkd = QKDProtocol()
        self.entanglement_generator = EntanglementGenerator()

        # Add nodes to the network
        self.network.add_node("Alice", (0, 0))
        self.network.add_node("Bob", (1, 1))
        self.network.add_node("Charlie", (2, 2))

        # Connect nodes
        self.network.connect_nodes("Alice", "Bob", 1)
        self.network.connect_nodes("Bob", "Charlie", 1)

    def test_qkd_integration(self):
        """Test the integration of QKD within the network."""
        key = self.qkd.generate_key()
        result = self.qkd.distribute_key("Alice", "Bob")
        self.assertTrue(result)

        # Verify that the key is successfully shared
        shared_key = self.qkd.get_shared_key("Alice", "Bob")
        self.assertEqual(shared_key, key)

    def test_entanglement_integration(self):
        """Test the integration of entanglement generation within the network."""
        pair = self.entanglement_generator.generate_entangled_pair()
        self.network.add_entangled_pair("Alice", "Bob", pair)

        # Verify that the entangled pair is correctly added to the network
        entangled_pairs = self.network.get_entangled_pairs("Alice", "Bob")
        self.assertIn(pair, entangled_pairs)

    def test_full_network_functionality(self):
        """Test the overall functionality of the full network."""
        message = "Hello, Quantum Network!"
        result = self.network.transmit_message("Alice", "Charlie", message)
        self.assertEqual(result, "Message transmitted successfully.")

if __name__ == '__main__':
    unittest.main()
