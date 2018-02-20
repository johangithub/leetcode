import math
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        d={}
        def dfs(node,level):
            if level in d:
                d[level].append(node.val)
            else:
                d[level] = [node.val]
            
            if node.right:
                dfs(node.right, level+1)
            if node.left:
                dfs(node.left, level+1)

        dfs(root, 0)
        ans=[]
        for i in range(len(d)):
            ans.append(sum(d[i])/len(d[i]))
        return ans
