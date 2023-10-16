#!/usr/bin/python3
"""Unittests for the base class."""
import unittest
import json
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Will do a number of tests to check if
    the class returns the right output of raises
    the expected exception.
    """

    def setUp(self):
        """Sets up the instances before each test."""
        self.base_object1 = Base(1)
        self.base_object2 = Base(2)
        self.base_object3 = Base(17)

    def tearDown(self):
        """Deletes the instances after each test."""

    def test_object_id(self):
        """Checks if the assigned id is the expected one."""
        self.assertEqual(self.base_object1.id, 1)
        self.assertEqual(self.base_object2.id, 2)
        self.assertEqual(self.base_object3.id, 17)

    def test_no_file(self):
        """Checks if an empty list is returned if a file
        does not exist.
        """
        self.assertEqual(self.base_object1.load_from_file(), [])
        self.assertEqual(self.base_object2.load_from_file(), [])
        self.assertEqual(self.base_object3.load_from_file(), [])

    def test_empty_string(self):
        """Checks if empty list is returned if string is empty
        or None.
        """
        json_string = ""

        self.assertEqual(self.base_object1.from_json_string(None), [])
        self.assertEqual(self.base_object1.from_json_string(json_string), [])

    def test_json_string(self):
        """Checks if the return value is correct if the string
        is present.
        """
        json_string = json.dumps([{'id': 1, 'width': 4, 'height': 5},
                                  {'id': 2, 'width': 7, 'height': 8}])

        self.assertEqual(Base.from_json_string(json_string), [{"id": 1, "width": 4, "height": 5},
                                                              {"id": 2, "width": 7, "height": 8}])

    def test_to_json_string(self):
        """Checks if the value returned is the correct
        json string representation.
        """
        self.assertEqual(Base.to_json_string({'id': 1, 'width': 4, 'height': 5}),
                         json.dumps({'id': 1, 'width': 4, 'height': 5}))


if __name__ == "__main__":
    unittest.main()
