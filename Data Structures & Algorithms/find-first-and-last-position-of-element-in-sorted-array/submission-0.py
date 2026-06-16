class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [-1,-1]

        res[0] = self.rangeSearch(nums,target,False)

        if res[0] != -1:
            res[1] = self.rangeSearch(nums,target,True)
        
        return res
    

    def rangeSearch(self,nums,target,flag):

        req_ind = -1

        l,r = 0,len(nums)-1

        while l <= r:

            mid = (l + r)//2

            if nums[mid] < target:
                l = mid+1
            
            elif nums[mid] > target:
                r = mid-1
            
            else:
                req_ind = mid
                if flag:
                    l = mid+1
                else:
                    r = mid-1
        
        return req_ind
        