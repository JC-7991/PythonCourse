'''
Problem:
Given two strings A and B, return whether or not A can be shifted some number of times
to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb,
return false.
'''

def shift(A: str, B: str) -> bool:
    return (A and B) and (len(A) == len(B) and (B in A * 2))

if __name__ == "__main__":
    print(shift("abcde", "cdeab"))