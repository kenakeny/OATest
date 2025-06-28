# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:#type: ignore
            res=[]
            def dfs(node,level):
                if not node:
                    return None
                if len(res)== level:
                    res.append([])
                res[level].append(node.val)
                dfs(node.left,level+1)
                dfs(node.right,level+1)
            dfs(root,0)
            return res
            '''basically we do an level order traversal by using dfs traversal
            what i essentially do is this:
            we call dfs (root,0) what happens here is as follows:
            if it's null we just stop
            if len(res)== level checks for how far we are, if its' a new depth we append to result a new list [] for this specific level 
            
            '''