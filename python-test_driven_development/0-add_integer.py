#!/usr/bin/python3
"""Module that defines a function to add two integers.

This module provides a simple integer addition function
that accepts integers and floats as input values.
"""


def add_integer(a, b=98):
    """Add two integers or floats and return an integer result.

    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
