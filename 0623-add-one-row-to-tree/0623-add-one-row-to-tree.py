# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        queue = deque([root])
        current_depth = 1
        
        while current_depth < depth - 1:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            current_depth += 1
        
        while queue:
            node = queue.popleft()
            self.insert_node(node, val, 'left')
            self.insert_node(node, val, 'right')
        
        return root
    
    def insert_node(self, node, val, direction):
        new_node = TreeNode(val)
        if direction == 'left':
            new_node.left = node.left
            node.left = new_node
        else:
            new_node.right = node.right
            node.right = new_node