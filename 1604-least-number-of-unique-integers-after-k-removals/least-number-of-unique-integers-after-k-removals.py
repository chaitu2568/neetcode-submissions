class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        dics = Counter(arr)
        minheap = [(count,value) for value,count in dics.items()]
        heapq.heapify(minheap)
        
        while k > 0 and minheap:
            curr_count,curr_val = heapq.heappop(minheap)
            if curr_count > k:
                heapq.heappush(minheap,(curr_count-k, curr_val))
            k -= curr_count
        return len(minheap)