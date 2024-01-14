#!/usr/bin/python3
def canUnlockAll(boxes):
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
