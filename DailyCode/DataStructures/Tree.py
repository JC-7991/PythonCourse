from __future__ import annotations
from typing import Any, Optional, Union

class Node:
    
    def __init__(self, val: int, left: Optional[Node] = None, right: Optional[Node] = None) -> None:
        self.val = val
        self.left = left