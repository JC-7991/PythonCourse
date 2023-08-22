from typing import Iterable

class Node:
    
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        
        if self.next:
            return f"{str(self.val)} => {str(self.next)}"
        
        return str(self.val)
    
class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.rear = None
        self.length = 0

    def __repr__(self) -> str:
        return str(self.head)
    
    def add(self, val: int = 0):

        if self.head == None:
            self.head = Node(val)
            self.rear = self.head
        
        else:
            self.rear.next = Node(val)