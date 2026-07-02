class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False for _ in nums]
        
        def backtrack(temp,nums,res,visited):
            if len(temp) == len(nums):
                res.append(list(temp))
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                temp.append(nums[i])
                backtrack(temp,nums,res,visited)
                visited[i] = False
                temp.pop()
        
        backtrack([],nums,res,visited)
        return res
    
        


        