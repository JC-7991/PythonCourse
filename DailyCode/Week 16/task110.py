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
    else:
        path.append(root.data)

    pathLen = pathLen + 1

    if root.left is None and root.right is None:
        printArray(path, pathLen)
    else:
        printPathRec(root.left, path, pathLen)
        printPathRec(root.right, path, pathLen)

def printArray(ints, len):
    for i in ints[0: len]:
        print(i, " ", end = "")
    print()