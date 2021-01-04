#运用中序遍历,即可得到结果
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归写法(顺序中序遍历,统计所有节点)
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res=[]
        def mid_search(root,res):
            if not root:
                return
            mid_search(root.left,res)
            res.append(root)
            mid_search(root.right,res)
        mid_search(root,res)
        return res[-k].val

#倒叙中序遍历,先访问右子树,再访问根节点,最后访问左子树,每访问到一个,k减少1
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k=k #定义全局变量
        def mid_search(root):
            if not root:
                return
            mid_search(root.right)
            self.k-=1
            if self.k==0:
                self.res=root.val
                return
            mid_search(root.left)
        mid_search(root)
        return self.res


#非递归写法
# class Solution:
#     def kthLargest(self, root: TreeNode, k: int) -> int:
#         res=[]
#         stack=[]
#         cur=root
#         while cur or stack:
#             if cur:
#                 stack.append(cur)
#                 cur=cur.left
#             else:
#                 top=stack.pop()
#                 res.append(top)
#                 cur=top.right
#         return res[-k].val