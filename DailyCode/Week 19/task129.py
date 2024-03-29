'''
Given a real number n, find the square root of n. For example, given n = 9, return 3.
'''

X = 10 ** (-6)

def almostEqual(num1: float, num2: float) -> bool:
    return num1 - X < num1 < num2 + X

def getSquare(num: int) -> float:
    
    high, low = num, 0

    while True:

        mid = ((high + low) / 2)
        mid_square = mid * mid

        if almostEqual(mid_square, num):
            return round(mid, 6)
        
        elif mid_square < num:
            low = mid + 1

        else:
            high = mid - 1

if __name__ == "__main__":
    print(getSquare(100))
    print(getSquare(9))