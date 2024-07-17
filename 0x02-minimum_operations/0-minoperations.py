#!/usr/bin/python3
"""
2. Minimum Operations
"""


def minOperations(x):  # x is the number
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file
        Returns:
            Integer: if n is impossible to acheive,
            return 0
    """
    res = 0  # result
    idx = 2  # index
    if x < 2:
        return 0
    while (idx < x + 1):
        # check to see if the problem can be broken into smaller problems
        while x % idx == 0:
            # if yes, then add no of smaller problems to result
            res += idx
            # break into smaller pieces
            x /= idx
        idx += 1
    return res
