# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        result=False
        if A and B: #如果A与B非空
            if A.val==B.val:
                result=self.a_equal_b(A,B)
            if result==False:
                result= self.isSubStructure(A.left,B) #从A的左子树寻找
            if result==False:
                result=self.isSubStructure(A.right,B) #还找不到就从A的右子树寻找
        return result

    def a_equal_b(self,a, b):  # 先判断两者是否有相同的根节点
        if b is None:
            return True
        if a is None:
            return False
        if a.val != b.val:
            return False
        return self.a_equal_b(a.left, b.left) and self.a_equal_b(a.right, b.right)


