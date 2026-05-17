class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        temp = {} #it stores last occurance of each char in the string
        for i in range(len(s)):
            temp[s[i]] = i
        
        start,end = 0,0
        res = []
        for i in range(len(s)):
            end = max(end, temp[s[i]])
            if i == end:
                res.append(end-start+1)
                start = i + 1
        return res
        