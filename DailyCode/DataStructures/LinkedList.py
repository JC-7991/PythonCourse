from typing import Iterable

class Node:
    
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        
        if self.next:
            return f"{str(self.val)} => {str(self.next)}"
        
        return str(self.val)