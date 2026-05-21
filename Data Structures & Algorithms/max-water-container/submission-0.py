class Solution:
    def maxArea(self, nums: List[int]) -> int:

        low, high = 0, len(nums)-1
    
        maxi = 0
        
        while low <= high:
            
            width = high - low
            area = width * min(nums[low],nums[high])
            maxi = max(area,maxi)
            
            if nums[low] < nums[high]:
                low += 1
            else:
                high -= 1
        
        return maxi
        