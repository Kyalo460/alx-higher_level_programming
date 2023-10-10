#!/usr/bin/python3
"""A module for opedning an printing files to stdout."""


def read_file(filename=""):
    """Will open and read a file."""

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print("{}".format(line), end='')
