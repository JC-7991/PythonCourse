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
            sum = sum + temp.data

            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)