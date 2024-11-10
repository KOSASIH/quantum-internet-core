# examples/repeater_network_example.py

from quantum_repeaters import QuantumRepeater  # Assuming this is the module for quantum repeaters

def repeater_network_example():
    """Example of a quantum repeater network with multiple nodes."""
    repeater = QuantumRepeater(num_nodes=5)

    # Distributing entanglement across the network
    repeater.distribute_entanglement()

    # Check the entanglement status of each node
    for node in repeater.nodes:
        print(f"Node {node.id} entangled: {node.is_entangled}")

    # Transmit a message through the repeater
    message = "Hello from the quantum repeater network!"
    result = repeater.transmit_message(message)
    print(result)

if __name__ == "__main__":
    repeater_network_example()
