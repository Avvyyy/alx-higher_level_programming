#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    no_of_args = len(sys.argv) - 1
    i = 1
    
    if no_of_args >  1:
        print("{} arguments:".format(no_of_args))
    elif no_of_args == 1:
        print("{} argument:".format(1))
    else:
        print("0 arguments.")

    for args in sys.argv[1:]:
        print("{:d}:".format(i), args)
        i += 1
