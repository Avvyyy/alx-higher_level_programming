#!/usr/bin/python3

"""Class Base"""

class Base:
    """
    Python class called Base

    Instances:
    nb_objects
    id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise a new base
        Args:
        id(int): Id of the base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
