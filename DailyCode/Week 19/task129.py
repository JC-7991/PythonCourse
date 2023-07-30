'''
Given a real number n, find the square root of n. For example, given n = 9, return 3.
'''

X = 10 ** (-6)

def almostEqual(num1: float, num2: float) -> bool:
    return num1 - X < num1 < num2 + X

def getSquare(num: int) -> float:
    
    high, low = num, 0

    while True:
        pass