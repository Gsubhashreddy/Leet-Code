# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res=[]
    def helper(self, root):
        if root==None:
            return
        if root.left == None and root.right ==None:
            self.res.append(root.val)
            return
        
        self.helper(root.left)
        self.helper(root.right)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.res=[]
        self.helper(root1)
        res1=self.res[:]
        self.res=[]
        self.helper(root2)
        res2=self.res
        if res1==res2:
            return True
        return False
        