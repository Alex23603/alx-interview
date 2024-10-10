def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    unlocked = [0]  # The first box is unlocked
    keys = set(boxes[0])  # Get keys from the first box
    visited = set([0])  # Mark box 0 as visited

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in visited:
            visited.add(key)
            keys.update(boxes[key])  # Add keys from the new box

    return len(visited) == len(boxes)
