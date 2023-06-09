'''
Given a set of closed intervals, find the smallest set of numbers that covers all the
intervals. If there are multiple smallest sets, return any of them.
For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers
that covers all these intervals is {3, 6}.
'''

from typing import List, Optional, Tuple

def span(intervals: List[List[int]]) -> Optional[Tuple]:
    
    if not intervals:
        return
    
    start = intervals[0][1]
    end = start
    cnt = 1

    for interval in intervals[1:]:

        int_start, int_end = interval
        
        if int_start < start and int_end < start:
            start = int_end
            cnt += 1

        else:
            break

    for interval in intervals[cnt:]:

        int_start, _ = interval

        if int_start > end:
            end = int_start
    
    return start, end

if __name__ == "__main__":

    print(span([[0, 3]]))
    print(span([[0, 3], [2, 6]]))
    print(span([[0, 3], [2, 6], [3, 4]]))
    print(span([[0, 3], [2, 6], [3, 4], [6, 7]]))
    print(span([[0, 3], [2, 6], [3, 4], [6, 9]]))
    print(span([[0, 3], [2, 6], [3, 4], [6, 100]]))
    print(span([[0, 4], [1, 2], [5, 6]]))