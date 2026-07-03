class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        nums.sort()

        visited = [False for _ in range(len(nums))]

        def backtrack(nums,visited,temp, res):

            if len(temp) == len(nums):
                res.append(list(temp))

            for i in range(len(nums)):

                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                
                visited[i] = True
                temp.append(nums[i])
                backtrack(nums,visited,temp,res)
                temp.pop()
                visited[i] = False

        res = []

        backtrack(nums,visited,[],res)

        return res


        