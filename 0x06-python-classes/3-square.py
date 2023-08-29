#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """square Class
    Attributes:
        __size (int): size of a side of the sqr
    """
    def __init__(self, size=0):
        """ initializes the sqr
        Args:
            size (int): size of a side of the sqr
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the sqr's area
        returns:
            The area of the sqr
        """
        return (self.__size) ** 2
