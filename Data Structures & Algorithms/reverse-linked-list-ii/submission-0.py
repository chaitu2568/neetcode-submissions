# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        
        curr = head
        prev = dummy
        
        l, r = left, right
        
        while l > 1:
            prev = curr
            curr = curr.next
            l -= 1
            r -= 1
            
        sub = curr
        
        prev1 = None
        while r > 0:
            prev1 = curr
            curr = curr.next
            r -= 1
        
        prev1.next = None
        reversed = self.rev(sub)

        prev.next = reversed
        sub.next = curr

        return dummy.next
  
  
    def rev(self, node):
        prev = None
        curr = node

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
        