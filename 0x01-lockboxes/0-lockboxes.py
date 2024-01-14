#!/usr/bin/python3
def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened.
    Args:
        boxes: list of lists
    Returns:
        True if all boxes can be opened, else return False
    """
    li = [0]
    lin = 0
    while (lin < 2):
        for i, w in enumerate(boxes):
            if i in li:
                for j in w:
                    li.append(j)
        lin += 1
    for i in range(len(boxes)):
        if i not in li:
            return False
    return True
