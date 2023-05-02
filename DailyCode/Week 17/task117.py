'''
Given a binary tree, return the level of the tree with minimum sum.
'''

from collections import deque

class Node:

    def __init__(self, key):
        self.data = key
        self.left = key
        self.right = key

def maxLvl(root):

    if root == None:
        return 0
    
    result = root.data

    q = deque()
    q.append(root)

    while(len(q) > 0):

        count = len(q)
        sum = 0
        
        while(count > 0):

            temp = q.popleft()
            sum += temp.data

            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)

            count -= 1
        
        result = max(sum, result)
    
    return result

if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7) 
    print("Maximum level sum is", maxLvl(root))