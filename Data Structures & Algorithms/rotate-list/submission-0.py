# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Write your code here
    
        if not head:
            return 
        
        size = 0
        
        curr = head
        while curr:
            size += 1
            curr = curr.next
            
        k = k % size  
        pos = size - k
        
    
        second = head
        prev = None
        while pos > 0:
            prev = second
            second = second.next
            pos -= 1
        
        prev.next = None
        
        if not second:
            return head
            
        curr2 = second
        prev2 = None
        
        while curr2:
            prev2 = curr2
            curr2 = curr2.next
    
        if prev2:
            prev2.next = head
            
        return second
        