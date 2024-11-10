# examples/entanglement_demo.py

from entanglement import EntanglementGenerator  # Assuming this is the module for entanglement generation

def entanglement_demo():
    """Demonstration of entanglement generation between two qubits."""
    generator = EntanglementGenerator()

    # Generate an entangled pair
    pair = generator.generate_entangled_pair()
    
    if pair.is_entangled:
        print("Entangled pair generated successfully!")
        print(f"Pair state: {pair.state}")
    else:
        print("Failed to generate entangled pair.")

if __name__ == "__main__":
    entanglement_demo()
