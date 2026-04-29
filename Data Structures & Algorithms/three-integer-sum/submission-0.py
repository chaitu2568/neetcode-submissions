class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
    
        low, high = 0, len(nums)-1
        
        res = []
        
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            first = -nums[i]
            
            low, high = i+1, len(nums)-1
            
            while low < high:
                
                if nums[low] + nums[high] == first:
                    
                    res.append([nums[low],nums[high],-first])
                    
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    
                    low += 1
                    high -= 1
                
                elif nums[low] + nums[high] < first:
                    low += 1
                else:
                    high -= 1
            
        return res
        