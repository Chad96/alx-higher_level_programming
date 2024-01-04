#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """Defines a rectangle with width and height attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return (str(self.print_symbol) * self.width + "\n") * self.height

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __gt__(self, other):
        """Greater than comparison"""
        if not isinstance(other, Rectangle):
            raise TypeError("Can't compare Rectangle with {}".format(type(other)))
        return self.area() > other.area()

    def __lt__(self, other):
        """Less than comparison"""
        if not isinstance(other, Rectangle):
            raise TypeError("Can't compare Rectangle with {}".format(type(other)))
        return self.area() < other.area()

    def __eq__(self, other):
        """Equal comparison"""
        if not isinstance(other, Rectangle):
            raise TypeError("Can't compare Rectangle with {}".format(type(other)))
        return self.area() == other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison"""
        if not isinstance(other, Rectangle):
            raise TypeError("Can't compare Rectangle with {}".format(type(other)))
        return self.area() >= other.area()

    def __le__(self, other):
        """Less than or equal to comparison"""
        if not isinstance(other, Rectangle):
            raise TypeError("Can't compare Rectangle with {}".format(type(other)))
        return self.area() <= other.area()

    def __ne__(self, other):
        """Not equal comparison"""
        if not isinstance(other, Rectangle):
            raise TypeError("Can't compare Rectangle with {}".format(type(other)))
        return self.area() != other.area()

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size"""
        return cls(size, size)
