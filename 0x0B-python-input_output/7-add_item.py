#!/usr/bin/python3
"""A method that will add strings to a list
in a file.
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""Will add arguments from the command line to the
json file.
"""

args = argv[1:]
j_list = list()

try:
    o_list = load_from_json_file('add_item.json')
except Exception:
    o_list = []

j_list += o_list
j_list += args

save_to_json_file(j_list, 'add_item.json')
