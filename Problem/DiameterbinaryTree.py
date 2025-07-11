# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # type: ignore
        leng=0
        def dfs(root):
            if not root:return 0
            nonlocal leng
            left=dfs(root.left)
            right = dfs(root.right)
            leng=max(leng,left+right)
            return 1+max(left,right)
        dfs(root)
        return leng