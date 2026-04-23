class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dics = set()

        for i in range(len(nums)):

            if nums[i] in dics:
                return True
            else:
                dics.add(nums[i])
        
        return False

        