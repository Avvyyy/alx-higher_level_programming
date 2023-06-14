#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())  # Sort the keys in alphabetical order
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
