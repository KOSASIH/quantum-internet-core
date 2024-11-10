# tests/unit/test_qkd.py

import unittest
from qkd import QKDProtocol  # Assuming this is the module for QKD protocols

class TestQKDProtocol(unittest.TestCase):
    def setUp(self):
        """Set up a QKDProtocol instance for testing."""
        self.qkd = QKDProtocol()

    def test_key_generation(self):
        """Test the key generation process."""
        key = self.qkd.generate_key()
        self.assertEqual(len(key), 128)  # Assuming a 128-bit key

    def test_key_distribution(self):
        """Test the key distribution process."""
        result = self.qkd.distribute_key("Alice", "Bob")
        self.assertTrue(result)

    def test_security_analysis(self):
        """Test the security analysis of the generated key."""
        key = self.qkd.generate_key()
        security_level = self.qkd.analyze_security(key)
        self.assertGreater(security_level, 0.8)  # Assuming a security threshold

if __name__ == '__main__':
    unittest.main()
