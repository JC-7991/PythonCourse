'''
Given an array of numbers representing the stock prices of a company in chronological
order and an integer k, return the maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it, and you must sell the stock before you
can buy it again.
For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
'''

from typing import List

def maxProfitHelper(

        arr: List[int],
        curr_index: int,
        curr_profit: int,
        buys_left: int,
        sells_left: int,
        length: int

) -> int:
    
    if curr_index == length or sells_left == 0:
        return curr_profit