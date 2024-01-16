#!/usr/bin/python3
"""
minOperations function
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters
    """

    if type(n) is not int or n < 2:
        return 0

    prime = 0
    count = 2

    while count <= n:
        if n % count == 0:
            prime += count
            n = n / count
        else:
            count += 1
    return prime
