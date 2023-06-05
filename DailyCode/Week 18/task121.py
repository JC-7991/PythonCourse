'''
Given a string which we can delete at most k, return whether you can make a palindrome.
For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get
'waterretaw'.
'''

def isPalin(string: str) -> bool:
    return string == string[::-1]

def makePalin(string: str, k: int) -> bool:
    if isPalin(string):
        return True