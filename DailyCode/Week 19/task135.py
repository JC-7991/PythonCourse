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
  pass