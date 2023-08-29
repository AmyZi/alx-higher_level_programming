#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """Square Class
    Attributes:
        __size (int): size of a side of the Square
    """
    def __init__(self, size=0):
        """initializes the Square
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
