#!usr/bin/python3
"""Integer addition function"""

def add_integer(a, b=98):
    """Return the integer of a and b.

    Float arguments are casted to ints before execution

    Raises:
        TypeError: if either a or b is a non_integer and non-float
    """
    if not isinstance (a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance (b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a)+int(b) )
