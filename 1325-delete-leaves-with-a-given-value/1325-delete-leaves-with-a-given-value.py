# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(head, target):
            if head == None:
                return True
            if head.left == None and head.right == None:
                if head.val == target:
                    return True
                else:
                    return False
            le = dfs(head.left, target)
            ri = dfs(head.right, target)
            if le:
                head.left = None
            if ri:
                head.right = None
            if le and ri and head.val == target:
                return True
            return False
        val = dfs(root, target)
        if val == True:
            return None
        return root
            
            
                
            
        