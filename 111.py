# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        levels = []
        def dfs(node,level):            
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
            if not (node.left or node.right):
                levels.append(level)
            
        dfs(root, 1)
        return min(levels)
