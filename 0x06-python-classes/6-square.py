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
            position (tuple): position of the square
        Returns:
            None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints the square area with the # character to stdout"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
