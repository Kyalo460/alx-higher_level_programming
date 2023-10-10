#!/usr/bin/python3
"""A function that writes to a file."""


def write_file(filename="", text=""):
    """Creates a newfile or overwrites the existing one."""

    chars = 0

    with open(filename, 'w', encoding='utf-8') as f:
        chars = f.write(text)

        return chars
