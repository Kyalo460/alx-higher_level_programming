#!/usr/bin/python3
"""A method that will append a certain line
after a line that contains a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Opens 'filename', searches for 'search_string' then
    adds 'new_string' after the line that has 'search_string.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        list_of_lines = f.readlines()

    new_list = []

    with open(filename, 'w', encoding='utf-8') as f:
        for line in list_of_lines:
            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)

        new_file_lines = "".join(new_list)
        f.write(new_file_lines)
