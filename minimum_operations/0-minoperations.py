#!/usr/bin/python3
"""
Module that contains minOperations function to calculate
minimum number of operations needed to reach n H characters
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): The desired number of H characters

    Returns:
        int: The minimum number of operations needed,
             returns 0 if n <= 1 or impossible
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                operations += n
            break

    return operations