class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归方法
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root


#迭代通过
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 0
        stack = [root]
        while stack:
            for i in range(len(stack)):
                top = stack.pop()
                top.left,top.right=top.right,top.left
                if top.left:
                    stack.append(top.left)
                if top.right:
                    stack.append(top.right)
        return root