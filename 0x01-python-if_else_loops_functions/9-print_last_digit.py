#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number > 0:
        last_digit = number % 10
    elif number < 0:
        number = abs(number)
        last_digit = number % 10
    return last_digit
 
