#方法一:递归方法
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        res=[]
        def inorder(root):
            if not root:
                return root
            else:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        return res

#方法二:迭代方法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





#自己的方法,未通过最后一个测试用例
class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        res=[]
        if not root:
            return res
        stack=[root,root]
        top=stack.pop()
        res.append(top.val)
        while stack:
            top=stack.pop()
            # res.append(top.val)
            if top.left:
                stack.append(top.left)
                res.insert(res.index(top.val)+1,top.left.val)
            if top.right:
                stack.append(top.right)
                res.insert(res.index(top.val),top.right.val)
        return res[::-1]

#正确方法思想
class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        res=[]
        if not root:
            return res
        stack=[]
        while stack or root:
            if root:#从根开始一直存在就向左下寻找
                stack.append(root)
                root=root.left
            else:#当左下到头后,开始从栈顶元素向右
                tmp=stack.pop()
                res.append(tmp.val)
                root=tmp.right
        return res




