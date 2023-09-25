#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """executes a function safely"""

    try:
        x = fct(*args)
        return x

    except Exception as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return None
