# network/quantum_network.py

import logging
from node import QuantumNode

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumNetwork:
    def __init__(self):
        """Initialize the quantum network with an empty list of nodes."""
        self.nodes = {}
        logging.info("Quantum network initialized.")

    def add_node(self, node_id, position):
        """Add a new quantum node to the network."""
        if node_id not in self.nodes:
            self.nodes[node_id] = QuantumNode(node_id, position)
            logging.info(f"Node {node_id} added at position {position}.")
        else:
            logging.warning(f"Node {node_id} already exists.")

    def remove_node(self, node_id):
        """Remove a quantum node from the network."""
        if node_id in self.nodes:
            del self.nodes[node_id]
            logging.info(f"Node {node_id} removed from the network.")
        else:
            logging.warning(f"Node {node_id} not found.")

    def get_node(self, node_id):
        """Retrieve a quantum node by its ID."""
        return self.nodes.get(node_id)

    def list_nodes(self):
        """List all nodes in the network."""
        return list(self.nodes.keys())
