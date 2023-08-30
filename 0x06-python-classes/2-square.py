#!/usr/bin/python3
"""this define a class Square."""


class Square:
    """this represent a square."""

    def __init__(self, size=0):
        """this initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("this size must be an integer")
        elif size < 0:
            raise ValueError("this size must be >= 0")
        self.__size = size

