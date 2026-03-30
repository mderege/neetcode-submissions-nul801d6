# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        r = []
        levelL = 0
        levelR = 0
        if root is not None:
            q.append(root)
        while len(q) > 0:
            curr = []
            l = len(q)
            for i in range(len(q)):
                c = q.pop(0)
                if i == l-1:
                    r.append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
                    
        return r
        # if level: is greater add the right side 