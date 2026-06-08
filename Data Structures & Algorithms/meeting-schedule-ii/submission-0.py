"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        #using min heap
    
        min_heap = []
        
        intervals.sort(key = lambda x:x.start)
        
        for i in range(len(intervals)):
            
            #If meeting which ends early is lessthan or equal to current meeting start time
            if min_heap and min_heap[0] <= intervals[i].start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,intervals[i].end)
            
        return len(min_heap)
        