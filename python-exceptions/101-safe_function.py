#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely and catches any exceptions.
    Args:
        fct: The function to execute.
        *args: Variable length argument list for the function.
    Returns:
        The result of the function if successful, otherwise None."""
    try:
        result = fct(*args)
        return result
    except Exception as error:
        # sys.stderr.write sends the output to the error stream
        sys.stderr.write("Exception: {}\n".format(error))
        return None
