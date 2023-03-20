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