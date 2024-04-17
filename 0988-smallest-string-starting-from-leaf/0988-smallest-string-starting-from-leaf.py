# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        result = None
        queue = deque([(root, '')])
        
        while queue:
            node, path = queue.popleft()
            current_path = chr(node.val + 97) + path  # Prepend the current character to path
            
            # Check if it is a leaf node
            if not node.left and not node.right:
                if result is None or current_path < result:
                    result = current_path
                    
            if node.left:
                queue.append((node.left, current_path))
            if node.right:
                queue.append((node.right, current_path))
                
        return result if result is not None else ''
                
                
                
        
        
        