#!/usr/bin/python3
# 7-islower.py


def islower(c):
    """This will Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
