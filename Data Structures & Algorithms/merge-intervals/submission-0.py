class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #sort the intervals by start time
        s_int = sorted(intervals, key = lambda x:x[0])

        res = [s_int[0]]
        
        for i in range(1,len(intervals)):
            
            curr = s_int[i]

            if curr[0] <= res[-1][1]:
                res[-1][1] = max(curr[1], res[-1][1])
            else:
                res.append(curr)
        
        return res


        