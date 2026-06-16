class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxheap = [-stone for stone in stones]

        heapq.heapify(maxheap)

        while len(maxheap) >= 2:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)

            if abs(x-y) != 0:
                heapq.heappush(maxheap,-abs(x-y))
        

        if not maxheap:
            return 0
        
        return -maxheap[0]
        