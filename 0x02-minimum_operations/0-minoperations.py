#!/usr/bin/python3
"""
0x03. Minimum Operations - determines minimum number of "copy all"/"paste"
operations to produce `n` number characters starting from 1.
"""

def minOperations(n):
    if not isinstance(n, int) or n < 2:
        return 0

    minOps = 0

    # within the potential factors of n, aside from 1
    for i in range(2, int(n**0.5) + 1):
        # for each factor found
        while n % i == 0:
            # add that to the total operations
            minOps += i
            # refocus to consider the remainder unprinted
            n //= i

    # If n is still greater than 1, it means n is a prime number
    if n > 1:
        minOps += n

    return minOps
