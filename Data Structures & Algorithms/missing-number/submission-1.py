class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            j = nums[i] # correct_index of current element
            if j < len(nums) and nums[i] != nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums) # for lst element ex: [0,1]
            

        