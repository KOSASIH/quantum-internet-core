# network/node.py

import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumNode:
    def __init__(self, node_id, position):
        """Initialize a quantum node with an ID and position."""
        self.node_id = node_id
        self.position = position
        self.connections = {}
        logging.info(f"Quantum node {node_id} created at position {position}.")

    def connect(self, other_node, distance):
        """Connect this node to another node with a specified distance."""
        self.connections[other_node.node_id] = distance
        other_node.connections[self.node_id] = distance
        logging.info(f"Node {self.node_id} connected to {other_node.node_id} with distance {distance}.")

    def get_neighbors(self):
        """Return a list of neighboring nodes."""
        return list(self.connections.keys())

    def get_distance(self, neighbor_id):
        """Return the distance to a neighboring node."""
        return self.connections.get(neighbor_id, float('inf'))

    def __repr__(self):
        return f"QuantumNode(id={self.node_id},position={self.position})"
