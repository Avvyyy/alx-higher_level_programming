#!/usr/bin/python3
"""Creation of class square"""

class Square(Rectangle):
    """
    Class Square that inherits from Rectangle

    Properties:
    size(int) - width and height of square
    x(int) - x-coordinate of Square
    y(int)- y-coordiate of square
    id(int) - Unique id of Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Declaration of propertes of Square

        Args:
        size
        x
        y
        id
        """

        super().__init__(self, size, size, x=0, y=0, id=None)

    @property
    def size_getter(self):
        """Getter for the size of square"""
        return self.width

    @size.setter
    def size_setter(self, value):
        """Setter for the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
            """
            Method to update the values of the properties of square
            
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
                        self.y == arg
                    count += 1

            elif kwargs and len(kwargs) != 0:
                for k, v in kwargs:
                    if k == "id":
                        if v is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = v
                    elif k == "size":
                        self.size = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v



    def to_dictionary(self):
        """Method to return the dictionary represenationof the properties"""
        return{
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
            }
