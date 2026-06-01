class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0
    
        start = 0
        max_char_count = 0
        maxi = 0
        
        dics = {}

        for end in range(len(s)):
            
            if s[end] not in dics:
                dics[s[end]] = 1
            else:
                dics[s[end]] += 1
            
            win_length = end-start+1
            max_char_count = max(max_char_count, dics[s[end]])
            
            if win_length - max_char_count > k:
                dics[s[start]] -= 1
                start += 1
            
            maxi = max(end-start+1, maxi)
        
        return maxi
        