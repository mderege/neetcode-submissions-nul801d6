# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def s(p, q):
            if not p and not q:
                return True
            
            if not p and q:
                return False
            if not q and p:
                return False
            
            if p.val != q.val:
                return False
            
            return s(p.left, q.left) and s(p.right, q.right)
        return s(p,q)