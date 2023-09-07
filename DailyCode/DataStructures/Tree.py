from __future__ import annotations
from typing import Any, Optional, Union

class Node:
    
    def __init__(self, val: int, left: Optional[Node] = None, right: Optional[Node] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: Any) -> bool:
        if type(other) == Node and self.val == other.val:
            return self.left == other.left and self.right == other.right
        return False
    
    def __repr__(self) -> str:
        return self.to_str()
    
    def height_helper(self) -> int:

        left_height = 0
        right_height = 0
        
        if self.left is not None:
            left_height = self.left.height_helper()

        if self.right is not None:
            right_height = self.right.height_helper()

        return max(left_height, right_height) + 1
    
    def insert_helper(self, val: int) -> None:
        
        if self.val > val:

            if self.left is None:
                self.left = Node(val)

            else:
                self.left.insert_helper(val)

        elif self.val < val:

            if self.right is None:
                self.right = Node(val)
                
            else:
                self.right.insert_helper(val)

    def num_nodes_helper(self) -> int:
        
        left = 0
        right = 0

        if self.left:
            left = self.left.num_nodes_helper()

        if self.right:
            right = self.right.num_nodes_helper()

        return left + right + 1