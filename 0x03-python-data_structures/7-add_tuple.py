#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a_extended = tuple_a + (0, 0)
    tuple_b_extended = tuple_b + (0, 0)

    # Compute the sum of the first elements and the sum of the second elements
    sum_first = tuple_a_extended[0] + tuple_b_extended[0]
    sum_second = tuple_a_extended[1] + tuple_b_extended[1]

    # Return the resulting tuple
    return sum_first, sum_second
