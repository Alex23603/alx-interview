#!/usr/bin/python3
def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    # Step 1: Precompute primes using the Sieve of Eratosthenes
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Precompute cumulative prime counts up to each index
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    # Step 2: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        # Total primes up to n determines the number of moves
        moves = prime_counts[n]
        if moves % 2 == 0:
            ben_wins += 1  # Ben wins if the number of moves is even
        else:
            maria_wins += 1  # Maria wins if the number of moves is odd

    # Step 3: Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
