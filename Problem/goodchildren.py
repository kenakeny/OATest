# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int: #type:ignore 
        # dfs but we keep track of the maximum value that has appeared so far
        def dfs(node,maxval):
            if not node:
                return 0
            if (node.val>=maxval):
                res=1
            else: res=0
            maxval=max(maxval,node.val)
            res+= dfs(node.left, maxval)
            res+=dfs(node.right,maxval)
            return res
        return dfs(root,root.val)