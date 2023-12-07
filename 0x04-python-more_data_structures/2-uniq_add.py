#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ add integers that only occur once"""
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
        
