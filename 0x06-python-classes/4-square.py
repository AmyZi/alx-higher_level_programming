#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A square class
    Attributes:
        __size (int): size of a side of a square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the square"s area
        Returns:
            The area of the sqr
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """get @ __size
        Returns:
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set @ __size
        Args:
            value (int): the size of a size of the sqr
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value