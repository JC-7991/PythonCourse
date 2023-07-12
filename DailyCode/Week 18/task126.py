'''
Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6]
rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of
the list. How many swap or move operations do you need?
'''

from typing import List

def rotate(arr: List[int], length: int) -> None:

    first = arr[0]
    for i in range(length - 1):
        arr[i] = arr[i + 1]
    arr[length - 1] = first

def rotate2(arr: list[int], k: int) -> List[int]:
    length = len(arr)