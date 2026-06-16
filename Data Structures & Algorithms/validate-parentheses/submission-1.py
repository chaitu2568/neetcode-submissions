class Solution:
    def isValid(self, s: str) -> bool:

        dics = {"{":"}","[":"]","(":")"}

        stack = []

        for ch in s:

            if ch in dics.keys():
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                last = stack.pop()

                if dics[last] != ch:
                    return False
        
        if stack:
            return False

        return True
