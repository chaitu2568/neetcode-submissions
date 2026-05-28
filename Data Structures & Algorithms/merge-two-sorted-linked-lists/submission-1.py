# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        
        if not list2:
            return list1

        first, second = list1, list2
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
        
        while first:
            curr.next = first
            first = first.next
            curr = curr.next
        
        while second:
            curr.next = second
            second = second.next
            curr = curr.next
        
        return prev.next
            





