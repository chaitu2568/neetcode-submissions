class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low, high = 0, len(nums)-1
    
        res = [0]*len(nums)
        curr = high
        while low <= high:
            if abs(nums[low]) > abs(nums[high]):
                res[curr] = nums[low]**2
                low += 1
            else:
                res[curr] = nums[high]**2
                high -= 1
            curr -= 1
        return res
            