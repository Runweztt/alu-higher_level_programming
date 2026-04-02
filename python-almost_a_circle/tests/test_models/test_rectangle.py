#!/usr/bin/python3
"""Unittest for Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic_creation(self):
        """Test basic Rectangle creation."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id_auto(self):
        """Test auto id."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_id_manual(self):
        """Test manual id."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width_type_error(self):
        """Test width TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_type_error(self):
        """Test height TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_x_type_error(self):
        """Test x TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_y_type_error(self):
        """Test y TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "1")

    def test_width_value_error(self):
        """Test width ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_height_value_error(self):
        """Test height ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_value_error(self):
        """Test x ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_value_error(self):
        """Test y ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update with kwargs."""
        r = Rectangle(10, 10)
        r.update(height=1, width=2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 2)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)
        self.assertEqual(d['x'], 1)
        self.assertEqual(d['y'], 9)
        self.assertEqual(d['id'], 1)

    def test_width_zero(self):
        """Test width zero raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        """Test height zero raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)


if __name__ == '__main__':
    unittest.main()
