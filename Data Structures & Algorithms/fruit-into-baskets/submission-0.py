class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        dics = {}
        maxi = 0
        
        for end in range(len(fruits)):
            ele = fruits[end]
            if ele not in dics:
                dics[ele] = 1
            else:
                dics[ele] += 1
            
            while start < end and len(dics) > 2:
                dics[fruits[start]] -= 1
                if dics[fruits[start]] == 0:
                    del dics[fruits[start]]
                start += 1
            
            maxi = max(maxi, end-start+1)
            
        return maxi
        