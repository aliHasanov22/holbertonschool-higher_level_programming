import sys


def safe_function(fct, *args):
    """ Executes a function safely and catches any exceptions.
    Args:
        fct: The function to execute.
        *args: Variable length argument list for the function.
    Returns:
        The result of the function if successful, otherwise None. """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        # Prints the exception message to stderr
        sys.stderr.write("Exception: {}\n".format(e))
        return None
