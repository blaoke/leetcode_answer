# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None: #如果这个树为空,返回True
            return True
        return self.sym(root.left,root.right) #遍历左子树和右子树

    def sym(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.val != root2.val:
            return False
        return self.sym(root1.left,root2.right) and self.sym(root1.right,root2.left)