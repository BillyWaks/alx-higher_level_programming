#!usr/bin/python3
"""Defines a function to print a square"""

def print_square(size):
    """Print a square
    
    Args:
        size(int): size length of square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")