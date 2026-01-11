#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """ Prints an integer with "{:d}".format().
    Args:
        value: The value to print (any type).
    Returns:
        True if value is an integer and was printed.
        False otherwise, printing the error to stderr. """

    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        # sys.stderr.write sends the message to the standard error stream
        sys.stderr.write("Exception: {}\n".format(e))
        return False
