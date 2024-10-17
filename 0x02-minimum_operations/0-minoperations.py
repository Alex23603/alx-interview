#!/usr/bin/python3
def minOperations(n):
    """Calculates the fewest number of operations to reach n characters using 'Copy All' and 'Paste'."""
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
