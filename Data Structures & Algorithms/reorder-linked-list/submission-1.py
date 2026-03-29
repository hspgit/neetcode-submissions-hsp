# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    

        # Snippet 2 (CORRECT REVERSAL)
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next      # Store next node
            second.next = prev   # Reverse current node's pointer
            prev = second        # Move prev to current node
            second = tmp         # Move to next node in original list
        
        first,second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
            
        
