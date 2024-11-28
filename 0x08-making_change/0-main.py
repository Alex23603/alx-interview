#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

# Test cases
print(makeChange([1, 2, 25], 37))  # Expected: 7 (25 + 10 + 2)
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected: -1
print(makeChange([1, 5, 10, 25], 63))  # Expected: 6 (25+25+10+1+1+1)
print(makeChange([1, 2, 5], 11))  # Expected: 3 (5+5+1)
print(makeChange([3, 7], 17))  # Expected: -1 (cannot meet total)