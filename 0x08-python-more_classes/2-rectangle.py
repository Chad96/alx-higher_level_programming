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
