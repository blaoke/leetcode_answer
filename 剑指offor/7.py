class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#前序遍历顺序为 [root,左子树，右子树]
#中序遍历顺序为 [左子树，root,右子树]

class Solution:
    def buildTree(self, preorder:list, inorder:list) -> TreeNode:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0]) #建立根节点
        index=inorder.index(root.val)  #得到根节点在中序遍历中的索引，以此来知道左子树有多少个节点
        root.left=self.buildTree(preorder=preorder[1:index+1],inorder=inorder[:index])
        root.right=self.buildTree(preorder=preorder[index+1:],inorder=inorder[index+1:])
        return root