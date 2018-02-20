# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d={}
        if not root:
            return []
        def dfs(node,level):
            print(node.val)
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
            ans.append(d[i])
        return ans
