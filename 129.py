# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans=[]
        q=[]
        def dfs(node):
            q.append(str(node.val))
            # if leaf
            if not (node.left or node.right):
                ans.append(int(''.join(q)))
                q.pop()
            # if not leaf
            else:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
                q.pop()
        if root:
            dfs(root)
        else:
            return 0
            
        return sum(ans)
