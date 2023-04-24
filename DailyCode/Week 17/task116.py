'''
Generate a finite, but an arbitrarily large binary tree quickly in O(1).
That is, generate() should return a tree whose size is unbounded but finite.
'''

import random

class Node:

    def __init__(self, val = 1, left = None, right = None):
        
        self.val = val
        self._left = left
        self._right = right
        self._isLeftEval = False
        self._isRightEval = False

    def left(self):
        if not self._isLeftEval:
            if random.random() < 0.5:
                self._left = Node()
            self._isLeftEval = True
        return self._left

    def right(self):
        if not self._isRightEval:
            if random.random() < 0.5:
                self._right = Node()
            self._isRightEval = True
        return self._right
    
    def generate():
        return Node()
    
    def traverse(node):
        if node == None:
            return 0