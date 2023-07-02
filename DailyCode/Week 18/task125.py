'''
Given the root of a binary search tree, and a target K, return two nodes in the tree
whose sum equals K.
For example, given the following tree and K of 20
    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
'''

class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BST:

  def __init__(self):
    self.root = None

  def insertR(self, root, data):

    if root is None:
      root = Node(data)
      return root
    
    if data < root.data:
      root.left = self.insertR(root.left, data)

    elif data > root.data:
      root.right = self.insertR(root.right, data)
      
    return root
  
  def insert(self, data):
    self.root = self.insertR(self.root, data)

  def ispair(self, root, temp, target):

    if temp is None:
      return False
    
    return self.search(root, temp, target - temp.data) or \ 
      self.ispair(root, temp.left, target) or \
      self.ispair(root, temp.right, target)