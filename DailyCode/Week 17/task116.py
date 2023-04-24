'''
Generate a finite, but an arbitrarily large binary tree quickly in O(1).
That is, generate() should return a tree whose size is unbounded but finite.
'''

import random

class Node:
    def __init__(self, val = 1, left = None, right = None):
        self.val = val