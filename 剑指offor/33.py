#利用二叉搜索树的特点,[左子树,右子树,根节点],判断列表是否满足
class Solution:
    def verifyPostorder(self, postorder:[int]) -> bool:
        n=len(postorder)
        root=postorder[-1]
        i=0
        while postorder[i]<root: #找到右子树的开始位置
            i+=1
        j=i
        for i in range(j,n): #如果右子树中有比根节点小的值,则返回False
            if postorder[i]<root:
                return False
        left=True
        if i>0:
            left=self.verifyPostorder(postorder[0:i])
        right=True
        if i<n-1:
            right=self.verifyPostorder(postorder[i:-1])
        return left and right

