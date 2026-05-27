# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = self.reverse(slow.next)
        slow.next = None
        
        curr = head
        while curr and second:
            temp = curr.next
            curr.next = second
            temp1 = second.next
            second.next = temp
            
            curr = temp
            second = temp1
        

    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        