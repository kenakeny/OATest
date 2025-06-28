class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        # swapping children for each root!!
        temp=root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
