# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        current = head
        while current is not None:
            stack.append(current)
            current = current.next
        
        size = len(stack)
        newHead = ListNode()
        newHeadCurrent = newHead
        current = head
        for idx in range(size):
            if idx % 2 == 0:
                newHeadCurrent.next = current
                current = current.next
            else:
                newHeadCurrent.next = stack.pop()
            newHeadCurrent = newHeadCurrent.next
        newHeadCurrent.next = None
        head = newHead.next
        return None