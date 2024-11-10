# network/routing.py

import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumRouting:
    def __init__(self, network):
        """Initialize the routing algorithm with a reference to the quantum network."""
        self.network = network

    def shortest_path(self, start_node_id, end_node_id):
        """Find the shortest path between two nodes using Dijkstra's algorithm."""
        unvisited = {node_id: float('inf') for node_id in self.network.list_nodes()}
        visited = {}
        current_node = start_node_id
        unvisited[current_node] = 0

        while unvisited:
            for neighbor in self.network.get_node(current_node).get_neighbors():
                if neighbor in unvisited:
                    tentative_value = unvisited[current_node] + self.network.get_node(current_node).get_distance(neighbor)
                    if tentative_value < unvisited[neighbor]:
                        unvisited[neighbor] = tentative_value

            visited[current_node] = unvisited[current_node]
            del unvisited[current_node]

            if not unvisited:
                break

            candidates = [node for node in unvisited.items() if node[1] != float('inf')]
            current_node = min(candidates, key=lambda x: x[1])[0]

        path = self.reconstruct_path(visited, start_node_id, end_node_id)
        logging.info(f"Shortest path from {start_node_id} to {end_node_id}: {path}")
        return path

    def reconstruct_path(self, visited, start_node_id, end_node_id):
        """Reconstruct the path from start to end node."""
        path = []
        current_node = end_node_id
        while current_node != start_node_id:
            path.append(current_node)
            current_node = min(visited, key=visited.get)
        path.append(start_node_id)
        return path[::-1]
