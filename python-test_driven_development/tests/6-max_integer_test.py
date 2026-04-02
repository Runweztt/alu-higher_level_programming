#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_regular_list(self):
        """Test with a regular list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max at beginning of list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with max in middle of list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with single element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_identical_elements(self):
        """Test with all identical elements."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == '__main__':
    unittest.main()
