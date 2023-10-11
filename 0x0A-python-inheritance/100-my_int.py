#!/usr/bin/python3
"""Will invert == with != ."""


class MyInt(int):
    """Returns the opposite of given
    operator.
    """

    def __eq__(self, value):
        """Inverts the equals operator."""
        return self.real != value

    def __ne__(self, value):
        """Inverts the not-equals to operator."""
        return self.real == value
