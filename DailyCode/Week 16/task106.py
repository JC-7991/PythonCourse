'''
Problem:
Given an integer list where each number represents the number of hops you can make,
determine whether you can reach to the last index starting at index 0.
For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
'''

from typing import List

def reach(arr: List[int]) -> bool:

    length = len(arr)
    cur_pos = 0
    last_ind = 0

    while cur_pos < length:
        if cur_pos == last_ind:
            return True
        elif arr[cur_pos]:
            return False
        cur_pos += arr[cur_pos]

    return False

if __name__ == "__main__":
    print(reach([2, 0, 1, 0]))
