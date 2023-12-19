#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    loop = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            loop += 1
    print()
    return loop
