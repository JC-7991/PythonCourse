'''
Problem:
Given a function f, and N return a debounced f of N milliseconds.
That is, as long as the debounced f continues to be invoked, f itself will not be
called for N milliseconds.
'''

from time import sleep
from typing import Any, Callable

def debounce(ms: int) -> Callable:
    pass