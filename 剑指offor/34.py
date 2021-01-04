#同题目113
#Python 赋值过程中不明确区分拷贝和引用，一般对静态变量的传递为拷贝，对动态变量的传递为引用,stack.copy 或者stack[:]可避免出来的数组全为空的情况
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
                    res.append(stack.copy()) #或者stack[:]
            if root.left:
                sums(root.left,sum-root.val,stack)
            if root.right:
                sums(root.right,sum-root.val,stack)
            stack.pop()
        sums(root,sum,stack)
        return res