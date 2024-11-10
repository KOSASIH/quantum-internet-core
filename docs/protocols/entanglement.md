# Entanglement Generation Protocols

Entanglement is a fundamental resource in quantum communication, enabling various applications such as quantum teleportation and superdense coding. This document outlines the protocols used for generating entangled states.

## Key Protocols

### 1. Bell State Generation

Bell states are specific maximally entangled quantum states of two qubits. The four Bell states are:

- \( |\Phi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle) \)
- \( |\Phi^-\rangle = \frac{1}{\sqrt{2}} (|00\rangle - |11\rangle) \)
- \( |\Psi^+\rangle = \frac{1}{\sqrt{2}} (|01\rangle + |10\rangle) \)
- \( |\Psi^-\rangle = \frac{1}{\sqrt{2}} (|01\rangle - |10\rangle) \)

#### Steps:
1. **Preparation**: A source generates pairs of entangled photons.
2. **Measurement**: The entangled photons can be measured by two parties (Alice and Bob) to verify entanglement.

### 2. Entanglement Swapping

Entanglement swapping allows two parties to become entangled without direct interaction.

#### Steps:
1. **Initial Entanglement**: Two pairs of entangled photons are created, one shared between Alice and Charlie, and the other between Bob and Charlie.
2. **Bell State Measurement**: Charlie performs a Bell state measurement on his two photons.
3. **Entanglement Establishment**: After the measurement, Alice and Bob become entangled, even though they never interacted directly.

## Applications

Entangled states are crucial for:
- Quantum Key Distribution (QKD)
- Quantum Teleportation
- Superdense Coding

## Implementation

The Quantum Internet Core includes implementations for Bell state generation and entanglement swapping. For usage examples, refer to the [usage documentation](usage.md).
