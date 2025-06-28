# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode: #type:ignore
        if not root or not p or not q:
            return None
        if (max(p.val,q.val) < root.val): return self.lowestCommonAncestor(root.left,p,q)
        elif (min(p.val,q.val) > root.val): return self.lowestCommonAncestor(root.right,p,q)
        else: return root
        #essentially this is a simple recursion algorithm what happens is that we try to find loewst common ancestor or the nearest ancestor since obviosuly the most common anscetor will be the root node
        #if its lower than the value we're at, we go left if its higher then we go right simple tree traversal