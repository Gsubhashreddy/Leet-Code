# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def dfs(head):
            nonlocal moves
            if head == None:
                return 0
            le = dfs(head.left)
            ri = dfs(head.right)
            
            moves += abs(le) + abs(ri)
            return (head.val-1) + le +ri
        dfs(root)
        return moves
            
        