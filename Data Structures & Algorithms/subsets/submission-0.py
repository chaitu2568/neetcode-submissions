class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums,temp,start,res):

            #add even empty subset
            res.append(list(temp))

            for i in range(start,len(nums)):
                temp.append(nums[i])
                backtrack(nums,temp,i+1,res)
                temp.pop()

        
        backtrack(nums,[],0,res)

        return res
        