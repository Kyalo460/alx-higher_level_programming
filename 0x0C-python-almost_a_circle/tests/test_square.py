#!/usr/bin/python3
"""Unittests for the square class."""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        """Sets up the objects of the class Square."""
        self.object1 = Square(2, 3, 1, 1)
        self.object2 = Square(7, 3, 2, 2)
        self.object3 = Square(1, 2, 0, 3)

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
            Square(-1, 1)

        with self.assertRaises(ValueError):
            Square(1, -1)

        with self.assertRaises(ValueError):
            Square(0, 1)

        with self.assertRaises(TypeError):
            Square("1", 2)

        with self.assertRaises(TypeError):
            Square(1, True)

        with self.assertRaises(ValueError):
            Square(1, 2, -1, 2)

        with self.assertRaises(ValueError):
            Square(-1, 2, 1)

        with self.assertRaises(TypeError):
            Square(1, 2, True, 2)

        with self.assertRaises(TypeError):
            Square(1, 2, '2', 1)

        with self.assertRaises(TypeError):
            Square(1.2, 1, 1, 3)

        with self.assertRaises(TypeError):
            Square(1, 2.0, 1, 3)

        with self.assertRaises(TypeError):
            Square(1, 2, 4.0, 2)

        with self.assertRaises(TypeError):
            Square(1, False, 4, 3)

    def test_area(self):
        """Checks if area returned is correct."""
        self.assertEqual(self.object1.area(), 4)

    def test_print(self):
        """Checks the string returned when the object
        is printed.
        """
        print_string = "[Square] (1) 3/1 - 2"
        self.assertEqual(str(self.object1), print_string)

    def test_update_args(self):
        """Check if the object has been updated with
        the correct values."""
        new_obj_string = "[Square] (10) 6/7 - 11"
        self.object1.update(10, 11, 6, 7)

        self.assertEqual(str(self.object1), new_obj_string)

    def test_update_kwargs(self):
        """Check if object was updated with **kwargs."""
        new_obj_string = "[Square] (2) 4/4 - 2"
        self.object2.update(id=2, size=2, x=4, y=4)

        self.assertEqual(str(self.object2), new_obj_string)

    def test_kwargs_skip(self):
        """Checks if **kwargs is skipped if *args is present in
        arguments passed to update().
        """

        new_obj_string = "[Square] (10) 6/4 - 5"
        self.object3.update(10, 5, 6, 4, id=1, width=5, height=6)

        self.assertEqual(str(self.object3), new_obj_string)

    def test_to_dictionary(self):
        """Tests the to_dictonary method that returns
        a dictionary representation of the object.
        """
        expected_dict = {'id': 1, 'size': 2, 'x': 3, 'y': 1}

        self.assertEqual(self.object1.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
