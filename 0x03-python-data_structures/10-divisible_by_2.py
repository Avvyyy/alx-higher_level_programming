#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    boolean_list = []

    for element in my_list:
        if element % 2 == 0:
           result =  True
        else:
            result += False
        boolean_list.append(result)
    return boolean_list
