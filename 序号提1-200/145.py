#二叉树后序遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归解法
class Solution:
    def postorderTraversal(self, root: TreeNode) -> [int]:
        res=[]
        self.posttorser(root,res)
        return res

    def posttorser(self,root,res:[]):
        if not root:
            return
        else:
            self.posttorser(root.left)
            self.posttorser(root.right)
            res.append(root.val)

#利用栈,迭代解法:
#先序是从右到左,后续与先序不同之处在于后续从左到右,最后得到的结果取逆
class Solution:
    def postorderTraversal(self, root: TreeNode) -> [int]:#二叉树的结构root为[1,null,2,3]
        res=[]
        stack=[root]#此时stack=[1]
        if not root:
            return res
        while stack:
            top=stack.pop()#此时top=[1,null,2,3]
            if top:
                res.append(top.val)#top.val表示top的第一个元素 即1
                if top.left:
                    stack.append(top.left)
                if top.right:
                    stack.append(top.right)
        res.reverse()#最后将数组取逆操作
        return res


