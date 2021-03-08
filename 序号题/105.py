#方法:使用递归调用方法, 从前序遍历和中序遍历的方法可以发现 前序遍历的第一个元素为根节点，而在后序遍历中，该根节点所在位置的左侧为左子树，右侧为右子树
#所以先根据前序遍历找到根节点然后找到中序遍历中根节点的位置,那么其左边的是根节点的左子树,右边的是根节点的右子树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root=preorder[0]
        root_index=inorder.index(root) #在中序遍历中找到根节点位置
        roots=TreeNode(root) #构造根节点
        roots.left=self.buildTree(preorder[1:root_index+1],inorder[:root_index]) #根节点的左子树
        roots.right=self.buildTree(preorder[root_index+1:],inorder[root_index+1:]) #根节点的右子树
        return roots
