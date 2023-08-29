#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """Square Class
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise Typeerror("size must be aan integar")
        else:
            self.__size = size
