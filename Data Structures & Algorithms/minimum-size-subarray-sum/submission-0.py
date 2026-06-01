class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        total = 0
        res = float("inf")
        
        for end in range(len(nums)):
            
            total += nums[end]
            
            while start <= end and total >= target:
                res = min(res,end-start+1)
                total -= nums[start]
                start += 1
        
        return 0 if res == float('inf') else res
        