# https://www.digitalocean.com/community/tutorials/how-to-write-doctests-in-python

import doctest

def add(a, b):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 4)
    6
    >>> add(2, 3)
    5
    """
    return a + b

doctest.testmod()

