#!/usr/bin/python3
"""Uses json serialzation to write objects to a file."""
import json


def save_to_json_file(my_obj, filename):
    """writes or overwrites an 'my_obj' to 'filename'."""

    j_string = json.dumps(my_obj)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(j_string)
