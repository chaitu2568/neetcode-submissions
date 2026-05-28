# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        
        # Replace this placeholder return statement with your code
        #sentinel node
        prev = ListNode()
        prev.next = head
        start = prev
        curr = head
        
        while curr:
            if curr.val == k:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
                
        return start.next
        