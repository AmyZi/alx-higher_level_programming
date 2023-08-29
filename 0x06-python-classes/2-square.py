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
            raise TypError("size must be aan integar")
        else:
            self.__size = size
