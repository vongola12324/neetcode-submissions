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
        if not head:
            return None
        
        m = {}
        current = head
        while current:
            m[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            m[current].next = m.get(current.next)
            m[current].random = m.get(current.random)
            current = current.next
        
        return m[head]
