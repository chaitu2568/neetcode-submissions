# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self,head):
    
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        temp = slow.next
        slow.next = None
        
        second = self.rev_list(temp)
        
        while first and second:
            
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        
        return True

    def rev_list(self,head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        