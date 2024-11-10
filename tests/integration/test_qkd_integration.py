# tests/integration/test_qkd_integration.py

import unittest
from network import QuantumNetwork  # Assuming this is the module for the quantum network
from qkd import QKDProtocol  # Assuming this is the module for QKD protocols

class TestQKDIntegration(unittest.TestCase):
    def setUp(self):
        """Set up a quantum network and QKD protocol for integration testing."""
        self.network = QuantumNetwork()
        self.qkd = QKDProtocol()

        # Add nodes to the network
        self.network.add_node("Alice", (0, 0))
        self.network.add_node("Bob", (1, 1))

        # Connect nodes
        self.network.connect_nodes("Alice", "Bob", 1)

    def test_qkd_key_distribution(self):
        """Test the key distribution process between two nodes."""
        result = self.qkd.distribute_key("Alice", "Bob")
        self.assertTrue(result)

        # Verify that the keys are shared
        key_a = self.qkd.get_shared_key("Alice", "Bob")
        key_b = self.qkd.get_shared_key("Bob", "Alice")
        self.assertEqual(key_a, key_b)

    def test_qkd_security_analysis(self):
        """Test the security analysis of the shared key."""
        self.qkd.distribute_key("Alice", "Bob")
        key = self.qkd.get_shared_key("Alice", "Bob")
        security_level = self.qkd.analyze_security(key)
        self.assertGreater(security_level, 0.8)  # Assuming a security threshold

if __name__ == '__main__':
    unittest.main()
