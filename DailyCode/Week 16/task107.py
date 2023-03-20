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

def printGivenLevel(root, level):
    if root is None:
        return root
    if level == 1:
        print(root.data, end = ' ')
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

def height(node):
    pass