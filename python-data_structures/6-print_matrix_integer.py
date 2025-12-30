#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for j in x:
            print("{:d}".format(j), end=" ")
        print()
