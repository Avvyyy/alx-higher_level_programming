#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """
    Program to writes JSON to a .txt

    Args:
    my_obj: Object to be cinverted to json
    filename: fiel tobe written to
    """

    my_json = json.dumps(my_obj)

    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(my_json)
