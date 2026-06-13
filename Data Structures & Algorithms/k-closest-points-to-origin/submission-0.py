class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        res = []
        
        for i in range(len(points)):
            
            heapq.heappush(maxheap,(-self.find_dist(points[i]),points[i]))
            
            if i > k-1:
                heapq.heappop(maxheap)
        
        while maxheap:
            res.append(heapq.heappop(maxheap)[1])
            
        return res

    def find_dist(self,point):
        return point[0]**2 + point[1]**2
            