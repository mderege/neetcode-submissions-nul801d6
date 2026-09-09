# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.curr = True 
        def b(root):
            if not root:
                return 0
            
            l = b(root.left)
            r = b(root.right)

            if (abs(l-r) > 1):
                self.curr =  False
            
            return max(l, r)+1
        b(root)
        return self.curr
        