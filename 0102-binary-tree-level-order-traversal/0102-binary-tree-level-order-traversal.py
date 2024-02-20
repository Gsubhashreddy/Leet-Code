# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def dfs(self, root, level):
        # Base
        if root == None:
            return
        if len(self.res) < level:
            # print(root.val, len(self.res), level)
            self.res.append([])
        self.res[level-1].append(root.val)
        
        # Logic
        
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.dfs(root, 1)
        return self.res
        