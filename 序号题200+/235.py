#因为是二叉搜索树所以只需要判断当前节点的值和所求两个节点的大小关系
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val<root.val and q.val<root.val:
           return self.lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val:
           return self.lowestCommonAncestor(root.right,p,q)
        else:#包括了p,q在root的两边这种情况 和 p或者q为root的情况
            return root