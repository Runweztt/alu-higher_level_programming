#!/usr/bin/python3
"""Module that defines a function to print a name.

This module provides a function that prints a formatted
name string with first and last name.
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Args:
        first_name: string for first name
        last_name: string for last name, defaults to empty string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
