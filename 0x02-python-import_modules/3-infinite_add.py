#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    i = 0

    for arg in sys.argv[1:]:
        i = i + int(arg)
    print(i)
