#!/usr/bin/python3
"""Unittests for the rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Tests for the rectangle class."""

    def setUp(self):
        """Sets up the objects of the class Rectangle."""
        self.object1 = Rectangle(2, 3, 1, 1, 1)
        self.object2 = Rectangle(7, 8, 2, 2, 2)
        self.object3 = Rectangle(1, 2, 0, 0, 3)

    def tearDown(self):
        """Deletes the instances that were set up."""
        del self.object1
        del self.object2
        del self.object3

    def test_exceptions(self):
        """Checks if the right exception is raised if invalid value
        is assigned.
        """
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)

        with self.assertRaises(ValueError):
            Rectangle(1, -1)

        with self.assertRaises(ValueError):
            Rectangle(0, 1)

        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, True)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 1, -2)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, True, 2)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 2, '1')

        with self.assertRaises(TypeError):
            Rectangle(1.2, 1, 1, 3)

        with self.assertRaises(TypeError):
            Rectangle(1, 2.0, 1, 3)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 4.0, 2)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 4, 3.0)

    def test_area(self):
        """Checks if area returned is correct."""
        self.assertEqual(self.object1.area(), 6)

    def test_print(self):
        """Checks the string returned when the object
        is printed.
        """
        print_string = "[Rectangle] (1) 1/1 - 2/3"
        self.assertEqual(str(self.object1), print_string)

    def test_update_args(self):
        """Check if the object has been updated with
        the correct values."""
        new_obj_string = "[Rectangle] (7) 2/2 - 4/4"
        self.object1.update(7, 4, 4, 2, 2)

        self.assertEqual(str(self.object1), new_obj_string)

    def test_update_kwargs(self):
        """Check if object was updated with **kwargs."""
        new_obj_string = "[Rectangle] (2) 4/4 - 2/2"
        self.object2.update(id=2, width=2, height=2, x=4, y=4)

        self.assertEqual(str(self.object2), new_obj_string)

    def test_kwargs_skip(self):
        """Checks if **kwargs is skipped if *args is present in
        arguments passed to update().
        """

        new_obj_string = "[Rectangle] (10) 3/4 - 5/6"
        self.object3.update(10, 5, 6, 3, 4, id=1, width=5, height=6)

        self.assertEqual(str(self.object3), new_obj_string)

    def test_to_dictionary(self):
        """Tests the to_dictonary method that returns
        a dictionary representation of the object.
        """
        expected_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 1, 'y': 1}

        self.assertEqual(self.object1.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
