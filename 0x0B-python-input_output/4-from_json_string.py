#!/usr/bin/python3

import json

def from_json_string(my_str):
    """
    Program  to return the python represenation of json

    Args;
    my_str
    """

    my_json = json.loads(my_str)
    return (my_json)
