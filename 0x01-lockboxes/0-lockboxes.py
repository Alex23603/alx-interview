#!/usr/bin/python3
"""
0-lockboxes module
This module defines a function that checks if all lockboxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    :param boxes: a list of lists, where each inner list represents the keys inside a box
    :return: True if all boxes can be opened, False otherwise
    """
    unlocked = set([0])  # Start by unlocking the first box
    keys = [0]  # List to store keys found in unlocked boxes

    while keys:
        current_key = keys.pop()  # Get a key
        for key in boxes[current_key]:  # For each key in the current box
            if key not in unlocked and key < len(boxes):  # Only consider keys to unopened boxes
                unlocked.add(key)  # Mark the box as unlocked
                keys.append(key)  # Add the key to explore further boxes

    # If all boxes are unlocked, the length of unlocked should match the total number of boxes
    return len(unlocked) == len(boxes)
