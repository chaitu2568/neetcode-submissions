class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        maxheap = [-num for num in nums]
    
        heapq.heapify(maxheap) #O(n)
        
        i = score = 0
        
        while i < k:
            curr = heapq.heappop(maxheap)
            score += -curr
            heapq.heappush(maxheap, -math.ceil(-curr / 3))
            i += 1
        
        return score
        