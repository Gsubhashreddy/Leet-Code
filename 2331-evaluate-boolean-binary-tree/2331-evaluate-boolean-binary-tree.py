# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        flag = False
        def dfs(head):
            nonlocal flag
            if head.left == None and head.right == None:
                return head.val
            le = dfs(head.left)
            if head.val == 2:
                if le ==1:
                    return 1
            ri = dfs(head.right)
            # print(head.val, le, ri)
            if head.val == 2:
                if le ==1 or ri ==1:
                    flag = True
                    return 1
            elif head.val == 3:
                if le ==1 and ri ==1:
                    flag = True
                    return 1
            return 0
        flag = dfs(root)
        if flag:
            return True
        return False