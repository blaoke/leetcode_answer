# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        stack=[] #存储单个满足条件的路径
        res=[] #存储所有路径
        if not root:
            return stack
        def sums(root,sum,stack):
            stack.append(root.val)
            if not root.left and not root.right:
                if root.val==sum:
                    res.append(stack.copy())
            if root.left:
                sums(root.left,sum-root.val,stack)
            if root.right:
                sums(root.right,sum-root.val,stack)
            stack.pop()
        sums(root,sum,stack)
        return res

