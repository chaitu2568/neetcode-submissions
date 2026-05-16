class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        first,second = m-1, n-1
        curr = m + n - 1
        while first >= 0 and second >= 0:

            if nums1[first] > nums2[second]:
                nums1[curr] = nums1[first]
                first -= 1
            elif nums2[second] > nums1[first]:
                nums1[curr] = nums2[second]
                second -= 1
            else:
                nums1[curr] = nums1[first]
                first -= 1
                second -= 1

            curr -= 1 
        
        while second >= 0:
            nums1[curr] = nums2[second]
            curr -= 1
            second -= 1
        



        






        