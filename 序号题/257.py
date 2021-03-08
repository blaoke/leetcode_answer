# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        res=[]
        if not root:
            return res
        if root.right==None and root.left==None:
            res.append(str ( root.val))
        leftres= self.binaryTreePaths(root.left)
        for i in range(len(leftres)):
            res.append(str(root.val)+'->'+str(leftres[i]))

        rightres = self.binaryTreePaths(root.right)
        for i in range(len(rightres)):
            res.append(str(root.val) + '->' + str( rightres[i]))
        return res
#容易理解的递归方法
class Solution:
    def __init__(self):
        self.res=[]
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        path=''
        def bfs(root,path):
            if not root:
                return self.res
            else:
                path+=str(root.val)
                if root.right==None and root.left==None:#如果当前节点是叶子节点
                    self.res.append(path)
                else:
                    path+='->'
                    bfs(root.left,path)
                    bfs(root.right,path)
        bfs(root,path)
        return self.res

#迭代方法,利用栈,开始栈中只有根节点,之后如果其子子树不是叶子节点就在栈中添加
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        if not root:
            return []
        stack=[(root,str(root.val))]
        res=[]
        while stack:
            node,val=stack.pop()#node表示返回的节点,val表示路径
            if node.right==None and node.left==None:#当节点为叶子节点时
                res.append(val)
            if node.right:#如果右子树存在
                stack.append((node.right,val+'->'+str(node.right.val)))
            if node.left:#如果左子树存在
                stack.append((node.left,val+'->'+str(node.left.val)))
        return res