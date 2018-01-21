"""
You need to find the largest value in each row of a binary tree.

Example:

Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""
#My solution using dictionary and dfs
def largestValues(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    d = {}
    def dfs(root, level):
        if root:
            if level not in d:
                d[level] = []
            d[level].append(root.val)
        if root.left:
            dfs(root.left, level+1)
        if root.right:
            dfs(root.right, level+1)
    if not root:
        return []
    dfs(root, 0)
    
    ans=[]
    for i in range(len(d)):
        ans.append(max(d[i]))
    return ans

# Divide and conquer one liner. Same concept, but optimized
def largestValues2(self, root):
    return [root.val] + map(max, *map(self.largestValues, (root.left, root.right))) if root else []


