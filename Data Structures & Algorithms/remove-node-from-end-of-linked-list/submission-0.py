# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or not head.next:
            return 
    
        size = 0
        
        curr = head
        while curr:
            curr = curr.next
            size += 1
        
        target = size - n
        
        if target == 0:
            return head.next
        
        prev = None
        curr1 = head
        while target > 0:
            prev = curr1
            curr1 = curr1.next
            target -= 1
        
        prev.next = curr1.next
        return head
        