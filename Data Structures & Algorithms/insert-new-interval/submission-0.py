class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        size = len(intervals)

        if size == 0:
            return [newInterval]

        res = []

        #add all meetings which ends before newInterval to res 

        i = 0

        while i < size and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # now add interval at the beginning and start merge all overlaps
        while i < size and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        res.append(newInterval)
        
        #add remaining
        while i < size:
            res.append(intervals[i])
            i += 1
        
        return res






        