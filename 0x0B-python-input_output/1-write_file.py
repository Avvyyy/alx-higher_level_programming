#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
    filename: File to be written into
    text: Text that will be written into the file

    Return:
    The number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        number_of_chars = f.write(text)

    return (number_of_chars)
