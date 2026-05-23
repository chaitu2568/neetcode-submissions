# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head
        prev = None
        
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        if n % 2 == 0:
            return slow.next
        
        return slow
        