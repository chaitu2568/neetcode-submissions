# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        res = lists[0]
        i = 1
 
        while i < len(lists):
            res = self.mergeLists(res,lists[i])
            i += 1
        
        return res

    def mergeLists(self,nums1, nums2):

        first, second = nums1, nums2

        prev = ListNode()
        curr = prev

        while first and second:

            if first.val <= second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            
            curr = curr.next
        
        if first:
            curr.next = first
    
        if second:
            curr.next = second
        
        return prev.next

