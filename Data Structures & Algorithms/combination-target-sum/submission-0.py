class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        
        def combSum(nums,temp,res,target, start):

            if target < 0:
                return

            if target == 0:
                res.append(list(temp))
                return
            
            #we start at the same index for next level of depth as it is mentioned we can use same number 
            for i in range(start, len(nums)):
                temp.append(nums[i])
                combSum(nums,temp,res,target-nums[i], i)
                temp.pop()
            
        combSum(nums,[],res,target,0)

        return res


        