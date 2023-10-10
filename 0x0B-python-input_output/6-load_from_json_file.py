#!/usr/bin/python3
"""Deserializing a json file."""
import json


def load_from_json_file(filename):
    """Open a file then use json to deserialize it."""

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
