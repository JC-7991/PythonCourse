'''
Problem:
Given a word W and a string S, find all starting indices in S which are anagrams of W.
For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
'''

from typing import Dict, List

def getFreq(string: str) -> Dict[str, int]:

    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq

def getWord(word: str, string: str) -> List[int]:
    
    wordLen = len(word)
    strLen = len(string)
    charMaster = getFreq(word)
    
    char = dict(charMaster)
    cnt = 0
    startInd = []

    if(wordLen > strLen) or (wordLen == 0):
        return []
    
    while(cnt < strLen):
        for i in range(cnt, strLen):
            if string[i] not in char:
                