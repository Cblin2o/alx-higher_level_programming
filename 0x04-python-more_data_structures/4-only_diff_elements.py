#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    difference = set()
    common = set()
    for i in (set_1,set_2):
        difference = (difference | i) - (i & common)
        common | = i
    return difference
