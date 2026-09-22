# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        dummy = tail = ListNode()
        while l1 and l2:
            value = l1.val + l2.val + extra
            if value >= 10:
                value -= 10
                extra = 1
            else:
                extra = 0
            tail.next = ListNode(value)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            value = l1.val + extra
            if value >= 10:
                value -= 10
                extra = 1
            else:
                extra = 0
            tail.next = ListNode(value)
            tail = tail.next
            l1 = l1.next
        while l2:
            value = l2.val + extra
            if value >= 10:
                value -= 10
                extra = 1
            else:
                extra = 0
            tail.next = ListNode(value)
            tail = tail.next
            l2 = l2.next
        if extra == 1:
            tail.next = ListNode(1)
        return dummy.next