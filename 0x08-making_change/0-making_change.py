#!/usr/bin/python3
"""
Module to solve the coin change problem using a greedy algorithm.
"""

def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount.

    Returns:
        int: Minimum number of coins needed to meet the total,
             or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)
    
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        # Use as many coins of the current denomination as possible
        num_coins += total // coin
        total %= coin

    # If total is not 0, it means it cannot be met by any combination of coins
    return num_coins if total == 0 else -1
