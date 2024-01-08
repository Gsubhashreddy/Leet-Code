# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    su=0
    def helper(self, root, low , high):
        if root==None:
            return
        if root.val<low:
            self.helper(root.right, low, high)
        elif root.val>high:
            self.helper(root.left, low, high)
        else:
            print(root.val)
            self.su+=root.val
            self.helper(root.left, low, high)
            self.helper(root.right, low, high)
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.su=0
        self.helper(root,low,high)
        return self.su
        