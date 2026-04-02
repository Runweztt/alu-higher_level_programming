#!/usr/bin/python3
"""Check inheritance only"""


def inherits_from(obj, a_class):
    """Returns True if inherited (not same class)"""
    return isinstance(obj, a_class) and type(obj) is not a_class
