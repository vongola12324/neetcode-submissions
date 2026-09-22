# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = current = None
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                minNode = p1
                flag = 1
            else:
                minNode = p2
                flag = 2

            if flag == 1:
                p1 = p1.next
            else:
                p2 = p2.next

            if head is None:
                head = current = minNode
            else:
                current.next = minNode
                current = minNode
                
        if p1 is not None:
            if head is None:
                head = p1
            else:
                current.next = p1
        if p2 is not None:
            if head is None:
                head = p2
            else:
                current.next = p2
            
        return head