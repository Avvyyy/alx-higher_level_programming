#!/usr/bin/python3
def islower(c):
    character = ord(c)
    if ord('a') <= character <= ord('z'):
        return True
    else:
        return False
