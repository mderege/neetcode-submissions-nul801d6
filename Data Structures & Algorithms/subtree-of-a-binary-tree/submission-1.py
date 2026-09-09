# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

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
        
        q = deque()
        if root:
            q.append(root)
        res = False
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.val == subRoot.val:
                    r = s(curr, subRoot)
                    res = r or res
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res
        