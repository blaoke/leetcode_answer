# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val==sum
        if root.left:
            self.hasPathSum(root.left,sum-root.val)
        if root.right:
            self.hasPathSum(root.right,sum-root.val)
        return False


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val==sum
        if self.hasPathSum(root.left,sum-root.val):
            return True
        if self.hasPathSum(root.right,sum-root.val):
            return True
        return False