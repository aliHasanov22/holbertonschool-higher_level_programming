#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = sys.argv
    if len(a) == 1:
        print("0 argument.")
    elif len(a) > 1:
        print("{} argument:".format(len(a)-1))
        for x in range(1, len(a)):
            print("{}: {}".format(x, a[x]))
