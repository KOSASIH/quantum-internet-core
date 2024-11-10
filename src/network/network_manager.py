# network/network_manager.py

import logging
from quantum_network import QuantumNetwork
from routing import QuantumRouting

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkManager:
    def __init__(self):
        """Initialize the network manager with a quantum network and routing instance."""
        self.network = QuantumNetwork()
        self.routing = QuantumRouting(self.network)
        logging.info("Network manager initialized.")

    def add_node(self, node_id, position):
        """Add a node to the quantum network."""
        self.network.add_node(node_id, position)

    def connect_nodes(self, node_id1, node_id2, distance):
        """Connect two nodes in the network."""
        node1 = self.network.get_node(node_id1)
        node2 = self.network.get_node(node_id2)
        if node1 and node2:
            node1.connect(node2, distance)
        else:
            logging.warning("One or both nodes not found.")

    def find_shortest_path(self, start_node_id, end_node_id):
        """Find the shortest path between two nodes."""
        return self.routing.shortest_path(start_node_id, end_node_id)

    def list_all_nodes(self):
        """List all nodes in the network."""
        return self.network.list_nodes()
