class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:#type: ignore
        def dfs(root):
            if not root:
                return [True,0]
            
            left,right=dfs(root.left),dfs(root.right)
            balancedT=left[0] and right[0] and (abs(left[1]-right[1])<=1)
            return [balancedT,1+max(left[1],right[1])]
        return dfs(root)[0]
        # did this in uni again, was fun remembering this question, understanding trees for the first time truly explodes your brain