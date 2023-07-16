#!/usr/bin/python3
"""Creation of class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle

    Properties:
    size(int) - width and height of square
    x(int) - x-coordinate of Square
    y(int)- y-coordinate of square
    id(int) - Unique id of Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Declaration of properties of Square

        Args:
        size (int): Size of the Square
        x (int): x-coordinate of the Square
        y (int): y-coordinate of the Square
        id (int): Unique id of the Square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Method to update the values of the properties of the square

        Args:
        *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents size attribute
            - 3rd argument represents x attribute
            - 4th argument represents y attribute
        **kwargs (dict): New key/value pairs of attributes.
        """

        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Method to return the dictionary representation of the properties"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
