#!/usr/bin/python3
"""A function to return serialized objects using json."""
import json


def to_json_string(my_obj):
    """Returns a json string."""

    return json.dumps(my_obj)
