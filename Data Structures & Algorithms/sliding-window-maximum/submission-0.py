class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        start = 0
    
        # To maintain monotonically decreasing queue where max element is always at start position for 
        # a given window
        q = collections.deque() # contains indexes
        
        res = []
        
        for end in range(len(nums)):
            
            # append to queue but before that check if last element in queue is less than current element and pop it out
            
            while len(q) > 0 and nums[q[-1]] < nums[end]:
                q.pop()
            
            q.append(end)
            
            #remove first element from the queue if start index cross the first element's index
            if start > q[0]:
                q.popleft() # this is the operation which is efficient and motivation behind to use deque instead of stack
            
            # if we reach window size shrink window
            if end >= k - 1:
                start += 1
                res.append(nums[q[0]])
        
        return res
        