#!/usr/bin/python3
"""A method that will add strings to a list
in a file.
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Will add arguments from the command line to the
    json file.
    """

    args = argv[1:]

    with open('my_list.json', 'w', encoding='utf-8') as f:
        j_list = load_from_json_file(f)

        if not isinstance(j_list, list):
            j_list = list()

        j_list += args

    save_to_json_file(j_list, 'my_list.json')
