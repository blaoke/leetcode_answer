#同主站104题
#方法一:使用递归解决
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         left_num=self.maxDepth(root.left)
#         right_num=self.maxDepth(root.right)
#         return max(left_num,right_num)+1

#方法二:用层次遍历解决
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         stack=[root]
#         res=0
#         while stack:
#             res+=1
#             for i in range(len(stack)):
#                 top=stack.pop(0)
#                 if top.left:
#                     stack.append(top.left)
#                 if top.right:
#                     stack.append(top.right)
#         return res

#方法三:使用回溯法解决

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res=[]
        self.maxs_len=0
        stack=[] #存储临时路径
        if not root:
            return len(res)
        def sums(root,res,stack):
            stack.append(root.val)
            if not root.left and not root.right:
                if len(stack[:])>self.maxs_len:
                    res.append(len(stack[:]))
                    self.maxs_len=len(stack[:])
            if root.left:
                sums(root.left,res,stack)
            if root.right:
                sums(root.right,res,stack)
            stack.pop()
        sums(root,res,stack)
        return res[-1]


