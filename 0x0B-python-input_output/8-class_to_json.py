#!/usr/bin/python3
"""Serializes a class to json."""
import json


def class_to_json(obj):
    """Will return a json dictionary tha represents the class's
    attributes.
    """

    json_string = json.dumps(obj, default=vars)
    return json.loads(json_string)
