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
            if node:
                q.append(str(node.val))
                # if leaf
                if not (node.left or node.right):
                    ans.append(int(''.join(q)))
                #if not leaf
                else: 
                    dfs(node.left)
                    dfs(node.right)
                q.pop()
        dfs(root)
            
        return sum(ans)
    
    # @caikehe recursion solution
    def sumNumbers(self, root):
        self.res = 0
        def dfs(node, value):
            if node:
                dfs(node.left, value*10+node.val)
                dfs(node.right, value*10+node.val)
                if not (node.left or node.right):
                    self.res += value*10+node.val
        dfs(root, 0)
        return self.res
