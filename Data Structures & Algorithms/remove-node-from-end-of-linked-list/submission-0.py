# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        current = head
        while current is not None:
            stack.append(current)
            current = current.next
        
        node = None
        for _ in range(n):
            node = stack.pop()

        if len(stack) == 0:
            head = node.next
        else:
            stack[-1].next = node.next

        return head