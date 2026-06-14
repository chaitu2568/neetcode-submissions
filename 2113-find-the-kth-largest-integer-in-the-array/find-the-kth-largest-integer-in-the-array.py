class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        maxheap = [-int(num) for num in nums]
        heapq.heapify(maxheap)

        curr = 0
        while k > 0:
            curr = heapq.heappop(maxheap)
            k -= 1
        
        return str(-curr)


             