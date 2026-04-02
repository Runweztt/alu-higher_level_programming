#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        """Test auto id assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_manual(self):
        """Test manual id assignment."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        """Test id is None increments counter."""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string(self):
        """Test to_json_string with data."""
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(result, '[{"id": 1}]')

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        """Test from_json_string with data."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(result, [{"id": 1}])


if __name__ == '__main__':
    unittest.main()
