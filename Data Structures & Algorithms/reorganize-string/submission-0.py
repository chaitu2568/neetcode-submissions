class Solution:
    def reorganizeString(self, s: str) -> str:
        dics = {}
    
        for ch in s:
            if ch in dics:
                dics[ch] += 1
            else:
                dics[ch] = 1
            
        maxheap = []
        res = []
        
        for key,value in dics.items():
            heapq.heappush(maxheap, (-value,key))
        
        while maxheap:
            
            curr_count, curr_val = heapq.heappop(maxheap)
            curr_count = -curr_count
        
            if res and res[-1] == curr_val:
                
                if not maxheap:
                    return ""
                
                #pop next ele
                next_count, next_char = heapq.heappop(maxheap)
                next_count = -next_count
                res.append(next_char)
                next_count -= 1
                if next_count  > 0:
                    heapq.heappush(maxheap,(-next_count,next_char))
            else:
                curr_count -= 1
                res.append(curr_val)
                
            if curr_count > 0:
                heapq.heappush(maxheap, (-curr_count,curr_val))
                
        return "".join(res)
        