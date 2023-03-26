'''
Problem:
Given a binary tree, return all paths from the root to leaves.
For example, given the tree
   1
  / \
 2   3
    / \
   4   5
it should return [[1, 2], [1, 3, 4], [1, 3, 5]].
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printPaths(root):
    path = []
    printPathRec(root, path, 0)
    
def printPathRec(root, path, pathLen):
    if root is None:
        return
    if(len(path) > pathLen):
        path[pathLen] = root.data