'''
You have a large array with most of the elements as zero.
Use a more space-efficient data structure, SparseArray, that implements the same interface:
init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
'''

from typing import List

class SparseArray:

    def __init__(self, arr: List[int], size: int) -> None:
        self.arr = {}
        self.size = size
        for index, val in enumerate(arr):
            