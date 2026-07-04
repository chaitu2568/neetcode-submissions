class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()
        
        def combSum(nums,temp,res,target, start):

            if target < 0:
                return

            if target == 0:
                res.append(list(temp))
                return
            
            #we start at the next index for next level of depth as it is mentioned we can use same number atmost once 
            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i-1]:
                    continue

                temp.append(nums[i])
                combSum(nums,temp,res,target-nums[i], i+1)
                temp.pop()
            
        combSum(nums,[],res,target,0)

        return res
        