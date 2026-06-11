class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #greedy approach to find min end time while you encounter an overlap
        intervals.sort(key = lambda x : x[0])

        prev = intervals[0]

        count = 0

        for i in range(1,len(intervals)):

            if prev[1] <= intervals[i][0]:
                prev = intervals[i]
            else:
                prev[1] = min(prev[1],intervals[i][1]) #greedy approach
                count += 1 
        
        return count

            

        