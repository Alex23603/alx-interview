def canUnlockAll(boxes):
    unlocked = set([0])
    keys = [0]  # Start with box 0
    
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)
    
    return len(unlocked) == len(boxes)
