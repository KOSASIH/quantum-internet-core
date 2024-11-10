# examples/simple_qkd_example.py

from qkd import QKDProtocol  # Assuming this is the module for QKD protocols

def simple_qkd_example():
    """A simple example of Quantum Key Distribution (QKD) between Alice and Bob."""
    qkd = QKDProtocol()

    # Alice and Bob generate and distribute keys
    result = qkd.distribute_key("Alice", "Bob")
    
    if result:
        key = qkd.get_shared_key("Alice", "Bob")
        print(f"Key successfully distributed: {key}")
    else:
        print("Key distribution failed.")

if __name__ == "__main__":
    simple_qkd_example()
