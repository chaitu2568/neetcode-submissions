class Solution:
    def validPalindrome(self, string: str) -> bool:

        left, right = 0, len(string)-1
  
        while left < right:
            
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return self.isPalin(string, left+1, right) or self.isPalin(string, left, right-1)
        
        return True
    
    def isPalin(self,nums, left, right):
        
        if len(nums) == 0:
            return True
        
        while left <= right:
            
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True