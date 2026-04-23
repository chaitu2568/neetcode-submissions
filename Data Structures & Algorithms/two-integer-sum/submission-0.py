class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in targetMap:
                targetMap[nums[i]] = i
            else:
                return [targetMap[diff], i]
        