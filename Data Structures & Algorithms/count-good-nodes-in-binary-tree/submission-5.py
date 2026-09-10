# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.mx = root.val

        def dfs(root):
            if not root:
                return 0
            total = 0
            
            if self.mx <= root.val:
                total +=1
                self.mx = root.val
            prev = self.mx
            c1 = dfs(root.left)
            
            self.mx = prev
            c2 =  dfs(root.right)
            return c1 + c2 + total
        
        return dfs(root)