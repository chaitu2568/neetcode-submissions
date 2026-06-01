class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        start = 0
        maxi = 0
        dics = {}

        for end in range(len(s)):

            if s[end] not in dics:
                dics[s[end]] = end
            
            else:
                if dics[s[end]] >= start:
                    start = dics[s[end]]+1
            
                dics[s[end]] = end
            
            maxi = max(maxi,end-start+1)
        
        return maxi
        