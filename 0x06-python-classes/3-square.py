#!/usr/bin/python3
"""Code to create a square class with size and area"""

class Square:
    """Class for a square"""
    def __init__(self, size=0):
        """
        Args:
        self
        size: size of aquare
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
            """Function to compute the area of a square with size instance"""
            square_area = self.__size**2
            return square_area
