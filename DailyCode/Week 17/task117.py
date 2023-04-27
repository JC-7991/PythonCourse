'''
Given a binary tree, return the level of the tree with minimum sum.
'''

from collections import deque

class Node:

    def __init__(self, key):
        self.data = key
        self.left = key
        self.right = key

def maxLvl(root):
    if root == None:
        return 0