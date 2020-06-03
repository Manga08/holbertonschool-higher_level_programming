#!/usr/bin/python3
"""The add attribute Module."""


def add_attribute(self, attribute, value):
    """Add attributes"""
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
