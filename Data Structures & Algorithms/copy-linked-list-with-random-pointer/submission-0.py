"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        od = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            od[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = od[curr]
            copy.next = od[curr.next]
            copy.random = od[curr.random]
            curr = curr.next
        
        return od[head]

