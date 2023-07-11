#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Program to return the JSON reresenation sof an object

    Args:
    my_obj
    """

    my_json = json.dumps(my_obj)
    return (my_json)
