#!/usr/bin/python3
"""Module that defines a function to print text with indentation.

This module provides a function that prints text with 2 new lines
after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    Args:
        text: string to print with indentation
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
