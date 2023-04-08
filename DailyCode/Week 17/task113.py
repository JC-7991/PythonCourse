'''
Problem:
Given a string of words delimited by spaces, reverse the words in string. For example,
given "hello world here", return "here world hello"
Follow-up: given a mutable string representation, can you perform this operation
in-place?
'''

def reverse(string: str) -> str:
    words = string.split()
    words.reverse()
    return " ".join(words)

if __name__ == "__main__":
    print(reverse("World! Hello"))