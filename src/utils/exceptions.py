# utils/exceptions.py

class QuantumNetworkError(Exception):
    """Base class for exceptions in the quantum network module."""
    pass

class NodeNotFoundError(QuantumNetworkError):
    """Exception raised when a node is not found in the network."""
    def __init__(self, node_id):
        self.node_id = node_id
        super().__init__(f"Node with ID '{node_id}' not found.")

class ConfigurationError(QuantumNetworkError):
    """Exception raised for errors in configuration."""
    def __init__(self, message):
        super().__init__(message)

class KeyStorageError(QuantumNetworkError):
    """Exception raised for errors in key storage operations."""
    def __init__(self, message):
        super().__init__(message)
