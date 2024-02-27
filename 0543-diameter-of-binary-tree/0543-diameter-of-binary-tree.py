# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def getHeight(self, root):
        # Base
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        
        # Logic
        le = self.getHeight(root.left)
        ri = self.getHeight(root.right)
        self.res = max(self.res, le + ri)
        return max(le, ri) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        self.getHeight(root)
        return self.res
        
        