#!/usr/bin/python3
"""this define a class Square."""


class Square:
    """this represent a square."""

    def __init__(self, size=0):
        """this initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("this size must be an integer")
        elif size < 0:
            raise ValueError("this size must be >= 0")
        self.__size = size

    def area(self):
        """this will return the current area of the square."""
        return (self.__size * self.__size)


