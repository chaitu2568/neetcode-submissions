class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        i = 0

        while i < len(nums):

            j = nums[i]-1

            '''
            this algorithm is similar to cyclic sort to find missing number from given range
            but here range can either go to negative numbers including 0 or numbers which are greater than
            length of array which we need to ignore
            '''

            if 0 < nums[i] <= len(nums) and nums[i] != nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
            
            else:
                i += 1
            
        
        for i in range(len(nums)):

            if nums[i] != i+1:
                return i+1
        
        #[1,2,3] is input then first missing positive is 4
        return len(nums) + 1
