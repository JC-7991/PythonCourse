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
    
    if root1 is None and root2 is None:
        return True
    
    if root1 is None or root2 is None:
        return False
    
    return (root1.data == root2.data and iden(root1.left, root2.left) and iden(root1.right, root2.right))

def subTree(T, S):
    
    if S is None:
        return True
    
    if T is None:
        return False
    
    if iden(T, S):
        return True
    
    return subTree(T.left, S) or subTree(T.right, S)

if __name__ == "__main__":

    T = Node(26)
    T.right = Node(3)
    T.right.right = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)

    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)

    if subTree(T, S):
        print("Tree 2 is subtree of Tree 1.")
    else:
        print("Tree 2 is not a subtree of Tree 1.")