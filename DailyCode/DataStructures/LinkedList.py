from typing import Iterable

class Node:
    
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.next = None

    def __repr__(self) -> None:
        pass