"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4]. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = {}
        def bfs(root, level):
            if level in ans:
                ans[level].append(root.val)
            else:
                ans[level] = [root.val]
            if root.left:
                bfs(root.left, level+1)
            if root.right:
                bfs(root.right, level+1)
        
        if root:
            bfs(root, 0)
        out=[]
        for i in list(ans):
            out.append(ans[i][-1])
        return out

    def rightSideView2(self, root):
        if not root:
            []
        right = self.rightSideView2(root.right)
        left = self.rightSideView2(root.left)
        return [root.val] + right + left[len(right):]

    def rightSideView3(self, root):
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)
        view = []
        collect(root, 0)
        return view

