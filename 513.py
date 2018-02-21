# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d={}
        def dfs(node, depth):
            if node:
                if depth in d:
                    d[depth].append(node.val)
                else:
                    d[depth] = [node.val]
                if node.left:
                    dfs(node.left, depth + 1)
                if node.right:
                    dfs(node.right, depth + 1)
        dfs(root, 0)
        return d[len(d)-1][0]
    
    # @StefanPochmann solution (BFS)
    def findLeftMostNode(self, root):
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val
    
    # @mayuecong solution (BFS)
    def findBottomLeftValue(self, root):
        queue=[root]; ans=0
        while any(queue):
            ans=queue[0].val
            queue=[leaf for node in queue for leaf in (node.left,node.right) if leaf]
        return ans
