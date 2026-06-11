class MedianFinder:

    def __init__(self):
        self.minheap = [] #stores larger numbers
        self.maxheap = [] #stores smaller numbers
        

    def addNum(self, num: int) -> None:

        #by default add first ele to max_heap or if current num is <= current max heaps largest 
        if not self.maxheap or -self.maxheap[0] >= num:
            heapq.heappush(self.maxheap, -num)
        else:
            #Push to min-heap
            heapq.heappush(self.minheap,num)
        
        #make sure you balance the heaps i.e by ensuring both heaps are either equal or diff by 1 during odd number cases
        if len(self.maxheap)-1 > len(self.minheap):
            ele = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-ele)
        
        elif len(self.maxheap) < len(self.minheap):
            ele = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-ele)
        

    def findMedian(self) -> float:
        l1 = len(self.minheap)
        l2 = len(self.maxheap)

        #if they are even
        if (l1+l2) % 2 == 0:
            return (self.minheap[0]+(-self.maxheap[0]))/2
        else: # if they are odd, get it queue which has more size
            return -self.maxheap[0]
        
        