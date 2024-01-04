#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """Defines a rectangle with width and height attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
