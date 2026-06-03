class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dics = {}
        start = 0
        for end in range(len(nums)):

            if nums[end] not in dics:
                dics[nums[end]] = end
            else:
                return True
            
            if end >= k:
                del dics[nums[start]]
                start += 1
            

        return False
            

        




        