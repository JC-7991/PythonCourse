'''
You have 100 fair coins and you flip them all at the same time. Any that come up tails
you set aside. The ones that come up heads you flip again. How many rounds do you
expect to play before only one coin remains?
Write a function that, given 'n', returns the number of rounds you'd expect to play
until one coin remains.
'''

from math import log2, ceil

def expectation(n: int) -> int:
    return ceil(log2(n + 1))

if __name__ == "__main__":

    print(expectation(0))
    print(expectation(1))
    print(expectation(2))
    print(expectation(100))
    print(expectation(200))