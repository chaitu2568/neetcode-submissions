class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        minheap = [(nums[i],i) for i in range(len(nums))]
        heapq.heapify(minheap)
        
        i = 0
        while i < k:
            curr,index = heapq.heappop(minheap)
            new = curr*multiplier
            heapq.heappush(minheap,(new,index))
            nums[index] = new
            i += 1
            
        return nums
        