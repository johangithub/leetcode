# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d={}
        if not root:
            return []

        def dfs(node,level):
            if level in d:
                d[level].append(node.val)
            else:
                d[level] = [node.val]
            
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)

        dfs(root, 0)
        ans=[]
        for i in range(len(d)):
            flip = 1 if i % 2 == 0 else -1
            ans.append(d[i][::flip])
        
        return ans
