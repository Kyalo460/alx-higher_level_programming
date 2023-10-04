#!/usr/bin/python3
"""Changes the format of a string."""


def text_indentation(text):
    """prints a text with 2 new lines after each
    of these characters: ., ? and :

    If text is not a string an exception is raised.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    j = ""
    for n in text:
        if j in [".", "?", ":"] and n == ' ':
            j = ""
            continue

        print("{:s}".format(n), end='')

        if n in [".", "?", ":"]:
            print()
            print()
            j = n
        else:
            j = ""
