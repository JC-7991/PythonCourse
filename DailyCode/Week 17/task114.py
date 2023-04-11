'''
Problem:
Given a string and a set of delimiters, reverse the words in the string while
maintaining the relative order of the delimiters. For example, given
"hello/world:here", return "here/world:hello"
Follow-up: Does your solution work for the following cases: "hello/world:here/",
"hello//world:here"
'''

from typing import Set

def revWords(string: str, delimiters: Set[str]) -> str:
    
    if len(string) == 0:
        return string
    
    words = []
    delims = []
    flagStart = string[0] in delimiters
    flagDelim = False
    currStr = ""

    for char in string:
        if char in delimiters:
            if flagDelim:
                currStr += 