#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    t = sys.argv[2]
    if t == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif t == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif t == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif t == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
