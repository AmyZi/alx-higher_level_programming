#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square Class
    Attributes:
        __size (int): size of a side of the Square
    """
    def __init__(self, size=0):
        """ initializes the Square
        Args:
            size (int): size of a side of the Square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the Square's area
        returns:
            The area of the Square
        """
        return (self.__size) ** 2
