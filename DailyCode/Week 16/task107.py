'''
Problem:
Print the nodes in a binary tree level-wise. For example, the following should print
1, 2, 3, 4, 5.
  1
 / \
2   3
   / \
  4   5
'''

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)
        print()

def printGivenLevel():
    pass

def height(node):
    pass