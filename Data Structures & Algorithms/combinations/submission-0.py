class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def combSum(nums,temp,res,start,k):

            if len(temp) == k:
                res.append(list(temp))
                return
            
            for i in range(start, len(nums)):
                temp.append(nums[i])
                combSum(nums,temp,res,i+1,k)
                temp.pop()
            
        combSum([i for i in range(1,n+1)],[],res,0,k)

        return res
        