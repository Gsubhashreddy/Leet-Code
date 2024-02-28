# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    
    def dfs(self, root, count, left):
        #Base
        if root == None:
            return
        if root.left == None and root.right == None:
            if len(self.res) == 0:
                self.res = [count, root.val]
            elif count > self.res[0]:
                self.res = [count, root.val]
            return
        
        # Logic
        self.dfs(root.left, count+1, True)
        self.dfs(root.right, count+1, False)
        
    
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = []
        self.dfs(root, 0, True)
        return self.res[1]
        
        