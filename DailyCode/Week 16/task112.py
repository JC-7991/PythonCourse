'''
Problem:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the
tree. Assume that each node in the tree also has a pointer to its parent.
According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined
between two nodes v and w as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself)."
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def findPath(root, path, k):
    
    if root is None:
        return False
    
    path.append(root.key)

    if root.key == k:
        return True