#!/usr/bin/python3
"""
Prime Game module.
Determines the winner of a prime number picking game.
"""

def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_count(n):
    """Counts the number of primes up to n."""
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return sum(primes)

def isWinner(x, nums):
    """
    Determines the winner of the game.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str or None: Name of the player with the most wins or None if tied.
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    max_num = max(nums)
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime(i) else 0)

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
