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
    
    if not k:
        return False
    
    for i in range(len(string)):
        if makePalin(string[:i] + string[i + k :], k - 1):
            return True
    
    return False

if __name__ == "__main__":
    print(makePalin("waterrfetawx", 2))