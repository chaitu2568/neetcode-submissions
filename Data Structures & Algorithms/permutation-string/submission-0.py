class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dics = {}
    
        k = len(s1)
        for ch in s1:
            if ch not in dics:
                dics[ch] = 1
            else:
                dics[ch] += 1
            
        
        start = 0
        curr_dist = 0
        
        for end in range(len(s2)):
        
            curr = s2[end]

            if curr in dics:
                dics[curr] -= 1
                if dics[curr] == 0:
                    curr_dist += 1
            
            if curr_dist == len(dics):
                return True
            
            if end >= k-1:
                if s2[start] in dics:
                    if dics[s2[start]] == 0:
                        curr_dist -= 1
                    dics[s2[start]] += 1
                start += 1
                    
        return False
        