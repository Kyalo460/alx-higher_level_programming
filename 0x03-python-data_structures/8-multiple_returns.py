#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns length of string and first character"""

    len_ = len(sentence)

    if len_ == 0:
        return (0, None)

    return (len_, sentence[0])
