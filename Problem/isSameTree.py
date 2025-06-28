# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # type: ignore
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
        #im ngl this is not a good solution but this is the first i came up with 
        #i'll try to make another one too 