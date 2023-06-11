#!/usr/bin/python3

def max_integer(my_list=[]):
    max_number = my_list[0]

    if len(my_list) == 0:
        return None
    else:
        for element in my_list[1:]:
            if element > max_number:
                max_number = element
        return max_number
