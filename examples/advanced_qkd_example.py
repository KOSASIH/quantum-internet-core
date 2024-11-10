# examples/advanced_qkd_example.py

from qkd import QKDProtocol  # Assuming this is the module for QKD protocols
from network import QuantumNetwork  # Assuming this is the module for the quantum network

def advanced_qkd_example():
    """An advanced example of QKD implementation with a quantum network."""
    network = QuantumNetwork()
    qkd = QKDProtocol()

    # Add nodes to the network
    network.add_node("Alice", (0, 0))
    network.add_node("Bob", (1, 1))
    network.add_node("Charlie", (2, 2))

    # Connect nodes
    network.connect_nodes("Alice", "Bob", 1)
    network.connect_nodes("Bob", "Charlie", 1)

    # Distribute keys between Alice and Bob
    result_ab = qkd.distribute_key("Alice", "Bob")
    if result_ab:
        key_ab = qkd.get_shared_key("Alice", "Bob")
        print(f"Key successfully distributed between Alice and Bob: {key_ab}")

    # Distribute keys between Bob and Charlie
    result_bc = qkd.distribute_key("Bob", "Charlie")
    if result_bc:
        key_bc = qkd.get_shared_key("Bob", "Charlie")
        print(f"Key successfully distributed between Bob and Charlie: {key_bc}")

if __name__ == "__main__":
    advanced_qkd_example()
