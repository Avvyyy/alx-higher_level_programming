#!/usr/bin/python3
"""Contains the function append_write"""


def append_write(filename="", text=""):
    """
     function that appends a string at the end of a text file (UTF8)
     and returns the number of characters added

     Args:
     filename: FIle to which data will be appended
     text: text to be appeneded to the file

     Return:
     The number of characters added
     """

    with open(filename, 'a', encoding='utf-8') as f:
        append_count = f.write(text)

    return (append_count)
