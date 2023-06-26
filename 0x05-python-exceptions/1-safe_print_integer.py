#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return_statement = True
    except ValueError:
        return_statement = False

    return return_statement
