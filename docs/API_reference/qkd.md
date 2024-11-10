# QKD API Reference

The QKD API provides functionalities for implementing Quantum Key Distribution protocols, such as BB84 and E91.

## Classes

### BB84

The `BB84` class implements the BB84 quantum key distribution protocol.

#### Methods

- **`__init__(self)`**
  - Initializes a new instance of the `BB84` protocol.

- **`generate_key(self, num_bits=100)`**
  - Generates a secure key using the BB84 protocol.
  - **Parameters**:
    - `num_bits` (int): The number of bits to generate (default is 100).
  - **Returns**: A string representing the generated key.

- **`measure(self, photon_state)`**
  - Measures the state of a photon and returns the result based on the chosen basis.
  - **Parameters**:
    - `photon_state` (str): The state of the photon to measure.
  - **Returns**: The measurement result (0 or 1).

#### Example Usage

```python
from qkd import BB84

# Initialize the BB84 protocol
qkd = BB84()

# Generate a secure key
key = qkd.generate_key(num_bits=256)
print("Generated Key:", key)
```

## E91
The E91 class implements the E91 quantum key distribution protocol.

### Methods
  - __init__(self)

  - Initializes a new instance of the E91 protocol.

- generate_key(self)

  - Generates a secure key using the E91 protocol.
  - Returns: A string representing the generated key.

### Example Usage

```python
1 from qkd import E91
2 
3 # Initialize the E91 protocol
4 e91 = E91()
5 
6 # Generate a secure key
7 key = e91.generate_key()
8 print("Generated Key:", key)
```
