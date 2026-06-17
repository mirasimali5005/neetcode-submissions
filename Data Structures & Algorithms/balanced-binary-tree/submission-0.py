class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root:
                return 0
            
            l = height(root.left)
            r = height(root.right)
            if l == -1 or r == -1:
                return -1
            if abs(l - r) > 1:
                return -1
            return 1 + max(l, r)
        
        return height(root) != -1