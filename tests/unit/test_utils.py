# tests/unit/test_utils.py

import unittest
from utils import UtilityFunctions  # Assuming this is the module for utility functions

class TestUtilityFunctions(unittest.TestCase):
    def test_calculate_distance(self):
        """Test the distance calculation between two points."""
        point_a = (0, 0)
        point_b = (3, 4)
        distance = UtilityFunctions.calculate_distance(point_a, point_b)
        self.assertEqual(distance, 5)

    def test_format_key(self):
        """Test the formatting of a key."""
        raw_key = "1234567890abcdef"
        formatted_key = UtilityFunctions.format_key(raw_key)
        self.assertEqual(formatted_key, "12:34:56:78:90:ab:cd:ef")

    def test_generate_random_key(self):
        """Test the generation of a random key."""
        key = UtilityFunctions.generate_random_key(128)
        self.assertEqual(len(key), 128)

if __name__ == '__main__':
    unittest.main()
