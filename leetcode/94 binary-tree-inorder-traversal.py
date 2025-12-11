class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def in_order_traversal(self, root) -> list[int]:
        res = []
        stack, node = [], root
        while stack or node:
            if node:
                stack.append(node)
            
    
        return res