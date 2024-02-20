# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # res = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return
        li = deque()
        li.append(root)
        res = []
        
        while li:
            size = len(li)
            temp = []
            for i in range(size):
                root = li.popleft()
                if root.left:
                    li.append(root.left)
                if root.right:
                    li.append(root.right)
                temp.append(root.val)
            res.append(temp)
        return res
                
        