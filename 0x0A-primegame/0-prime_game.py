#!/usr/bin/python3
def isWinner(x, nums):
    """Determines the winner of the Prime Game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    # Sieve of Eratosthenes
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Precompute the number of primes up to each index
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None