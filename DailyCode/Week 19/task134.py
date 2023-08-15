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
            if val != 0:
                self.arr[index] = val

    def __repr__(self) -> str:

        string = ""

        for pos in range(self.size):
            if pos in self.arr:
                string += f"{self.arr[pos]}, "
            else:
                string += "0, "