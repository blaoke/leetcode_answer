#二叉树先序遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归方法:
class Solution:
    def preorderTraversal(self, root: TreeNode) -> [int]:
        res=[]
        self.preorder(root,res)
        return res

    def preorder(self,root,res:[]):
        if not root:
            return
        else:
            res.append(root.val)
            self.preorder(root.left,res)
            self.preorder(root.right,res)

#迭代方法:
class Solution:
    def preorderTraversal(self, root: TreeNode) -> [int]:#二叉树的结构root为[1,null,2,3]
        res=[]
        stack=[root]#此时stack=[1],root表示二叉树的根节点
        if not root:
            return res
        while stack:
            top=stack.pop()#此时top=[1,null,2,3]
            if top:
                res.append(top.val)#top.val表示top的第一个元素 即1
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
        return res
