#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
the = "and is less than 6 and not 0"
b = -(a)
if number < 0:
    print("Last digit of {} is {} {}".format(number, b, the))
if a > 5 and number > 0:
    print("Last digit of {} is {} and is greater than 5".format(number, a))
elif a == 0:
    print("Last digit of {} is {} and is 0".format(number, a))
elif a < 6 and number > 0:
    print("Last digit of {} is {} {} ".format(number, a, the))
