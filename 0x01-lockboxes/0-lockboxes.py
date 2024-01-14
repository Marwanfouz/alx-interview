#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Function that checks with boolean value if the list type and
    length to invoke two for iterations one to traverse the list
    and the other to compaer if key is idx or not in order to open
    """
    opened_boxes = set()
    queue = [0]
    while queue:
        current_box = queue.pop(0)
        opened_boxes.add(current_box)
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                queue.append(key)
    return len(opened_boxes) == len(boxes)
