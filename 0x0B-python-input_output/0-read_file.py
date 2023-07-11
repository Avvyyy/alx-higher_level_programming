#!/usr/bin/python3
def read_file(filename=""):
    """
    Python file that reads a .txt and prints it to stdout

    Args:
    filename: FIlename of text file to be read

    Print:
    Content of text file
    """

    with open(filename, encoding="utf-8") as txt_file:
        file_content = txt_file.read()

    print(file_content, end="")
