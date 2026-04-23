class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dics = {}

        for ch in s:
            if ch not in dics:
                dics[ch] = 1
            else:
                dics[ch] += 1

        for ch in t:
            if ch in dics:
                dics[ch] -= 1
            else:
                return False
        
        for ch in dics:
            if dics[ch] != 0:
                return False
        
        return True
        
        
        