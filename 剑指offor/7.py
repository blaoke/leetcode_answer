class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder:list, inorder:list) -> TreeNode:
        if not preorder or inorder:
            return None
        root=preorder.pop(0)
        index=inorder.index(root)
        root.left=self.buildTree(preorder=preorder[:index],inorder=inorder[:index])
        root.right=self.buildTree(preorder=preorder[index:],inorder=inorder[index+1:])
        return root