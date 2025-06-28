# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: #type: ignore
        if not subRoot:
            return True
        if not root:
            return False
        if self.SameTree(root,subRoot):
             return True
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
    #LOLL I WAS DEBUGGING THIS FOR 10 MINS BECAUSE I WAS CALLING SAME TREE INSTEAD OF SUBTREE AT THE END HAHA
  
    def SameTree(self,f:Optional[TreeNode], s:Optional[TreeNode])->bool:#type: ignore
        if not f and not s:
            return True

        if f and s and (s.val==f.val):
             return (self.SameTree(f.left,s.left) and 
             self.SameTree(f.right,s.right))
        return False
