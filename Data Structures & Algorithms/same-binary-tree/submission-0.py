# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def walk(self, node: Optional[TreeNode]) -> list:
        result = []
        if node:
            result.append(node.val)
            result.extend(self.walk(node.left))
            result.extend(self.walk(node.right))
        else:
            result.append(None)

        return result

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pl = self.walk(p)
        ql = self.walk(q)

        return pl == ql
        