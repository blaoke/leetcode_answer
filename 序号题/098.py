# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#迭代方法解决
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack=[(root,float('-inf'),float('inf'))]
        while stack:
            top,mi,mx=stack.pop()#top表示栈顶元素,mi表示需要满足的最小元素,mx表示需要满足的最大元素
            val=top.val
            if val<=mi or val>=mx:#将当前值与条件最大值和最小值进行比较
                return False
            if top.right:
                stack.append((top.right,val,mx))
            if top.left:
                stack.append((top.left,mi,val))
        return True

#递归方法解决
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        def valid(root,mi=float('-inf'),mx=float('inf')):
            if not root:
                return True
            val=root.val
            if val<=mi or val>=mx:
                return False
            # 必须在root.left root.right都成立时才满足
            return valid(root.left,mi=mi,mx=val) and valid(root.right,mi=val,mx=mx)
        return valid(root)