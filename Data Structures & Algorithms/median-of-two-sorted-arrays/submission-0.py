class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        res = []

        i,j = 0,0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1

            else:
                res.append(nums2[j])
                j += 1

        if nums1:
            res.extend(nums1[i:])

        if nums2:
            res.extend(nums2[j:])

        mid = len(res)//2

        if len(res) % 2:
            return res[mid]

        else:
            return (res[mid-1]+res[mid])/2

        