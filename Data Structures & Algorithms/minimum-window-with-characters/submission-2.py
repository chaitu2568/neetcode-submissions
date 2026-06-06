class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        res = [len(s)+1 , 0, 0]

        t_count = {}

        for ch in t:

            if ch not in t_count:
                t_count[ch] = 1
            else:
                t_count[ch] += 1
        
        win_count = {}

        start = end = 0
        char_count = 0

        while end < len(s):

            if s[end] not in win_count:
                win_count[s[end]] = 1
            else:
                win_count[s[end]] += 1
            
            if s[end] in t_count and t_count[s[end]] == win_count[s[end]]:
                char_count += 1
            
            while start <= end and char_count == len(t_count):

                if end-start+1 < res[0]:
                    res = [end-start+1, start, end]
                
                win_count[s[start]] -= 1

                if s[start] in t_count and win_count[s[start]] < t_count[s[start]]:
                    char_count -= 1
                
                start += 1
            
            end += 1
    
        return s[res[1]:res[2]+1] if res[0] <= len(s) else ""       