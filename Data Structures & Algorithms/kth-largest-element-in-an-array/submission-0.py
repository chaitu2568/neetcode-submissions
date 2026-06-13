class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minheap = []
        i = 0

        while i < k:
            heapq.heappush(minheap,nums[i])
            i += 1
        
        while i < len(nums):

            heapq.heappush(minheap,nums[i])

            if i >= k-1:
                heapq.heappop(minheap)
            
            i += 1
        
        return minheap[0]


        