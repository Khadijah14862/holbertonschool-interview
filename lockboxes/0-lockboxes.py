#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened."""
    if not boxes:
        return True

    unlocked = {0}
    keys = [0]

    while keys:
        box_index = keys.pop()

        for key in boxes[box_index]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == len(boxes)
