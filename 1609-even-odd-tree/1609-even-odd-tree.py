# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q= deque()
        if root == None:
            return True
        flag = True
        odd = False
        q.append(root)
        while q:
            size = len(q)
            maxi = float('inf')
            mini = -1
            for i in range(size):
                ele = q.popleft()
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                if odd:
                    if ele.val % 2 !=0:
                        return False
                    if ele.val >= maxi:
                        return False
                    maxi = ele.val
                else:
                    if ele.val % 2 ==0:
                        return False
                    if ele.val <= mini:
                        return False
                    mini = ele.val
            odd = not odd
        return True
        