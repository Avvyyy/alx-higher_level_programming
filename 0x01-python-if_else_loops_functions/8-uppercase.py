#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_val = ord(c)
        if 97 <= ascii_val <= 122:
            ascii_val -= 32
        print(chr(ascii_val), end="")
    print()
