#!/usr/bin/python3
"""a module for opening boxes
"""

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is unlocked initially

    stack = [0]  # Use a stack to keep track of boxes to process

    while stack:
        current_box = stack.pop()  # Get a box to process
        for key in boxes[current_box]:  # Iterate through the keys in the current box
            if key < n and not unlocked[key]:  # Check if the key opens a valid and locked box
                unlocked[key] = True  # Unlock the box
                stack.append(key)  # Add the newly unlocked box to the stack

    return all(unlocked)  # Return True if all boxes are unlocked, else False

