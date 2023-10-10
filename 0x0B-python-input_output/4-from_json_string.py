#!/usr/bin/python3
"""Using json to unserialize a jsn string."""
import json


def from_json_string(my_str):
    """Returns an object(python data structure)."""

    return json.loads(my_str)
