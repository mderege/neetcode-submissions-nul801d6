# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxHeight = 0
        def t(root):
            nonlocal maxHeight
            if not root:
                return 0

            l = t(root.left)
            r = t(root.right)
            maxHeight = max(maxHeight, l+r)
            return max(l, r)+1
        t(root)
        return maxHeight

        