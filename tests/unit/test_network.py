# tests/unit/test_network.py

import unittest
from network import QuantumNetwork  # Assuming this is the module for the quantum network

class TestQuantumNetwork(unittest.TestCase):
    def setUp(self):
        """Set up a QuantumNetwork instance for testing."""
        self.network = QuantumNetwork()
        self.network.add_node("Node1", (0, 0))
        self.network.add_node("Node2", (1, 1))

    def test_add_node(self):
        """Test adding a node to the network."""
        self.network.add_node("Node3", (2, 2))
        self.assertIn("Node3", self.network.list_nodes())

    def test_remove_node(self):
        """Test removing a node from the network."""
        self.network.remove_node("Node1")
        self.assertNotIn("Node1", self.network.list_nodes())

    def test_shortest_path(self):
        """Test finding the shortest path between nodes."""
        self.network.connect_nodes("Node1", "Node2", 1)
        path = self.network.routing.shortest_path("Node1", "Node2")
        self.assertEqual(path, ["Node1", "Node2"])

if __name__ == '__main__':
    unittest.main()
