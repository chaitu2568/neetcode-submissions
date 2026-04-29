class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 0:
            return True

        result = ''.join(char for char in s if char.isalnum()).lower()

        left,right = 0,len(result)-1
 
        while left <= right:
            if result[left] == result[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True
            
        