#!/usr/bin/python3
"""Unittest for max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class will have functions that test if the integer
    returned is actually the max value.
    """

    def test_max(self):
        """Test whether the value returned is correct."""
        self.assertEqual(max_integer([1, 2, 3, 4]), max([1, 2, 3, 4]))
        self.assertEqual(max_integer([0.1, 0.2, 1.1]), max([0.1, 0.2, 1.1]))

    def test_empty(self):
        """Should return None if given empty list."""
        self.assertEqual(max_integer([]), None)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_one_element(self):
        """Tests a list with one value."""
        self.assertEqual(max_integer([2]), 2)


if __name__ == "__main__":
    unittest.main()
