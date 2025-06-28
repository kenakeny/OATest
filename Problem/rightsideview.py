class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: #type:ignore
        res=[]
        def dfs(node,level):
            if not node:
                return None
            if len(res)== level:
                res.append(node.val)
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        dfs(root,0)
        return res
    #neetcode was actually cooked in this regard so i didnt understand the problem right at first