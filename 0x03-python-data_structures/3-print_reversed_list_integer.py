#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """printn list in reverse"""
    if not my_list:
        pass
    else:
        for i in reversed(my_list):
            print("{:d}".format(my_list[i]))