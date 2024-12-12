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

    # Precompute primes
    primes = [i for i in range(max_n + 1) if sieve[i]]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Simulate the game for the current `n`
        moves = set(range(1, n + 1))
        turn = 0  # Maria starts

        while True:
            # Find the smallest prime in the remaining numbers
            valid_prime = next((p for p in primes if p in moves), None)
            if valid_prime is None:
                # No moves left, current player loses
                if turn % 2 == 0:  # Maria's turn
                    ben_wins += 1
                else:  # Ben's turn
                    maria_wins += 1
                break

            # Remove the prime and its multiples
            multiples = set(range(valid_prime, n + 1, valid_prime))
            moves -= multiples

            # Switch turns
            turn += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
