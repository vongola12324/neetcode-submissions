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
        m = {}
        current = head
        idx = 0
        nodeList = []
        while current:
            m.update({id(current): idx})
            nodeList.append(Node(current.val))
            current = current.next
            idx += 1            
        nodeList.append(None)
        
        current = head
        for idx, n in enumerate(nodeList):
            if n is None:
                break
            randomIdx = m.get(id(current.random), len(nodeList) - 1)
            n.next = nodeList[idx+1]
            n.random = nodeList[randomIdx]
            current = current.next

        return nodeList[0]
