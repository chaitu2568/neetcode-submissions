# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        curr = dummy

        while curr:

            # check first if curr can parse atleast k nodes, else break it
            temp = curr

            for _ in range(k):

                temp = temp.next

                if temp is None:
                    break
                
            
            if temp is None:
                break
            
            # reverse k nodes start from curr (not upto to end of whole size)
            reversed, next_group_start = self.rev(curr.next,k)

            end_of_prev_group = curr.next
            end_of_prev_group.next = next_group_start
            curr.next = reversed
            curr = end_of_prev_group
        
        return dummy.next

    
    def rev(self, node, k):
        prev = None
        curr = node

        while k > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1
        
        return prev, curr

        