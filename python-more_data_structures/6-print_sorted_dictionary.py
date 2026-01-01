#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for x in a_dictionary:
        b = a_dictionary.get(x)
        print("{}: {}".format(x, b))
