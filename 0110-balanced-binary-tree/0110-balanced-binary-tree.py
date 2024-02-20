# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateHeight(self, root):
        # Base
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        
        
        # Logic
        l = self.calculateHeight(root.left)
        r = self.calculateHeight(root.right)
        if l == -1 or r == -1:
            return -1
        else:
            if abs(l - r) <=1:
                return max(l,r) +1
            else:
                return -1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # At Every Root, we need to get LEFT tree hight and right Tree Hight 
        # Check if their heights > 1
        # Return False if Yes
        if root == None:
            return True
        res = self.calculateHeight(root)
        if res == -1:
            return False
        return True