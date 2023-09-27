'''
Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
'''

from typing import List, Tuple
from DataStructures.Tree import BinaryTree, Node

def min_path_sum_helper(node: Node) -> Tuple[int, List[int]]:
  
  left_sum, left = None, None
  right_sum, right = None, None

  if node.left:
    left_sum, left = min_path_sum_helper(node.left)
  if node.right:
    right_sum, right = min_path_sum_helper(node.right)

  if not left and not right:
    return node.val, [node.val]
  
  elif left and not right:
    return (left_sum + node.val), left + [node.val]
  
  elif right and not left:
    return (right_sum + node.val), right + [node.val]