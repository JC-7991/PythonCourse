'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same
structure and node values with a subtree of s. A subtree of s is a tree consists of a
node in s and all of this node's descendants. The tree s could also be considered as a
subtree of itself.
'''

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def iden(root1, root2):
    pass