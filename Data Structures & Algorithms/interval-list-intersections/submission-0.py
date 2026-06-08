class Solution:
    def intervalIntersection(self, interval_list_a: List[List[int]], interval_list_b: List[List[int]]) -> List[List[int]]:
        interval_list_a.sort(key = lambda x:x[0])
        interval_list_b.sort(key = lambda x:x[0])
        
        i = j = 0
    
        res = []
        
        while i < len(interval_list_a) and j < len(interval_list_b):
            first = interval_list_a[i]
            second = interval_list_b[j]
            
            overlap = [max(first[0], second[0]), min(first[1], second[1])]
            
            if overlap[0] <= overlap[1]:
                res.append(overlap)
                
            if first[1] < second[1]:
                i += 1
            else:
                j += 1
        
        return res
            