'''
Given a sorted list of integers, square the elements and give the output in sorted
order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
'''

from typing import List

Array = List[int]

def mergeLists(arr1: Array, arr2: Array) -> Array:
    
    ptr1, len1 = 0, len(arr1)
    ptr2, len2 = 0, len(arr2)
    mergeArray = []

    while ptr1 < len1 and ptr2 < len2:

        if arr1[ptr1] < arr2[ptr2]:
            mergeArray.append(arr1[ptr1])
            ptr1 += 1

        else:
            mergeArray.append(arr2[ptr2])
            ptr2 += 1
    
    mergeArray.extend(arr1[ptr1:])
    mergeArray.extend(arr2[ptr2:])
    return mergeArray

def sortSquared(arr: Array) -> Array:
    
    pos = 0
