# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        numsD = {}
        if len(preorder) == None:
            return None
        result = TreeNode(preorder[0])
        for i in range(len(inorder)):
            numsD[inorder[i]] = i

        def main(preorder, inorder, i):
            for i in range(len(inorder)):
                numsD[inorder[i]] = i
            if len(inorder) <= 0:
                return None
            k = numsD[preorder[0]]
            curr=TreeNode(preorder[0])
            curr.left = main(preorder[1:k+1], inorder[:k],i+1)
            curr.right = main(preorder[k+1:], inorder[k+1:], i+1)

            return curr
        return main(preorder,inorder, 0)