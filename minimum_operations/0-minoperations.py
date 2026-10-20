#!/usr/bin/python3
"""Calculate the minimum number of operations to reach n H characters."""


def minOperations(n):
    """Return the minimum number of Copy All and Paste operations."""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations
