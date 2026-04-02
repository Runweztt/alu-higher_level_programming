#!/usr/bin/python3
"""Module that defines a function to print a square.

This module provides a function that prints a square
made of # characters of a given size.
"""


def print_square(size):
    """Print a square of # characters with given size.

    Args:
        size: integer size length of the square
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
