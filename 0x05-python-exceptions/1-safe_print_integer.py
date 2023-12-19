#!/usr/bin/python3
def safe_print_integer(value):
    if (value % 1 == 0):
        try:
            print("{:d}".format(value))
        else:
            print("{}".format(value))
    return value
