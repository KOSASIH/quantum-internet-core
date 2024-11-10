# Quantum Key Distribution (QKD) Protocols

Quantum Key Distribution (QKD) is a method used to securely distribute cryptographic keys between two parties, leveraging the principles of quantum mechanics. The primary goal of QKD is to ensure that any eavesdropping attempts can be detected, providing a high level of security.

## Key Protocols

### 1. BB84 Protocol

The BB84 protocol, proposed by Charles Bennett and Gilles Brassard in 1984, is one of the first and most widely studied QKD protocols. It uses the polarization states of photons to encode bits.

#### Steps:
1. **Preparation**: The sender (Alice) prepares a series of photons in one of four polarization states.
2. **Transmission**: Alice sends the photons to the receiver (Bob).
3. **Measurement**: Bob randomly chooses a basis to measure each photon.
4. **Key Generation**: After transmission, Alice and Bob communicate over a classical channel to compare their bases and keep only the bits where they used the same basis.

### 2. E91 Protocol

The E91 protocol, proposed by Artur Ekert in 1991, uses entangled photon pairs to establish a secure key.

#### Steps:
1. **Entanglement Generation**: Alice and Bob share a pair of entangled photons.
2. **Measurement**: Each party measures their photon in a randomly chosen basis.
3. **Key Generation**: The results of their measurements are compared to generate a shared key. The correlations in their measurements provide security against eavesdropping.

## Security Considerations

QKD protocols are designed to be secure against various attacks, including:
- **Eavesdropping**: Any attempt to intercept the key will disturb the quantum states, alerting Alice and Bob.
- **Man-in-the-Middle Attacks**: Proper authentication methods must be employed to prevent such attacks.

## Implementation

The Quantum Internet Core provides implementations of the BB84 and E91 protocols. For usage examples, refer to the [usage documentation](usage.md).
