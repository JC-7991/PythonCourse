'''
Problem:
Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should
be swapped, the 3rd and 4th bit should be swapped, and so on.
For example, 10101010 should be 01010101. 11100010 should be 11010001.
Bonus: Can you do this in one line?
'''

def swapBits(num: int) -> int:
    filter_mask = 85
    return ((num & filter_mask) << 1) | ((num & (filter_mask << 1)) >> 1)

if __name__ == "__main__":
    print("Swapped: ", bin(swapBits(0)))