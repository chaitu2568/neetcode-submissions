class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ""
    
        first, second = 0,0
        
        while first < len(word1) and second < len(word2):
            res += word1[first]
            res += word2[second]
            first += 1
            second += 1
        
        if first < len(word1):
            res += word1[first:]
        
        if second < len(word2):
            res += word2[second:]
        
        return res
            