# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp = sp = head
        while fp and sp:
            sp = sp.next
            fp = fp.next
            if fp is not None:
                fp = fp.next
            else:
                break
            if fp and sp and fp.val == sp.val:
                return True
        
        return False