# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.dfs(root, [], res, sum)
        return res
    def dfs(self, root, ls, res, sum):
        if not root.left and not root.right and root.val==sum:
            res.append(ls+[root.val])
            return
        sum -= root.val
        if root.left:
            self.dfs(root.left, ls+[root.val], res, sum)
        if root.right:
            self.dfs(root.right, ls+[root.val], res, sum)