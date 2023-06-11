#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    boolean_list = []

    for element in my_list:
        if element % 2 == 0:
           boolean_list += True
        else:
            boolean_lit += False
    return boolean_list
