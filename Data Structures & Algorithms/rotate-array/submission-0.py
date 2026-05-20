class Solution:
    def rotate(self, nums, k):
        s = len(nums)
        k %= s
        self.reverse(nums, 0, s-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, s-1)
    
    
    def reverse(self, nums, i, j):
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        