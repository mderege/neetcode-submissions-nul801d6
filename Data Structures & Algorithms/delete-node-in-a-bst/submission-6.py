class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None:
                if root.right == None:
                    return None
                else:
                    return root.right
            elif root.right == None:
                if root.left == None:
                    return None
                else:
                    return root.left
            else:
                minVal = self.findMin(root.right)
                root.val = minVal
                root.right = self.deleteNode(root.right, minVal)
                
        return root
    def findMin(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val