#!/usr/bin/python3
"""python"""


def read_file(filename=""):
    """this is document"""
    with open(filename, "r", encoding="uft-8") as f:
        print(f.read(), end="")
