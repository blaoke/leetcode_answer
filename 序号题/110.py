class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res=True
        def depth(root):
            if not root:
                return 0
            left=depth(root.left)
            right=depth(root.right)
            diff=left-right
            if abs(diff)>1:
                self.res=False
            return max(left,right)+1
        depth(root)
        return self.res