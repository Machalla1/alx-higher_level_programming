#!/usr/bin/python3
"""this define a class Square."""


class Square:
    """this represent a square."""

    def __init__(self, size):
        """this will Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """this will get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("this size must be an integer")
        elif value < 0:
            raise ValueError("this size must be >= 0")
        self.__size = value

    def area(self):
        """this will return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """this will print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

