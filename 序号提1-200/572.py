#同剑指offor第26题
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        result=False
        if s :
            if s.val==t.val:
                result=self.equal_tree(s,t)
            if result==False:
                result=self.isSubtree(s.left,t)
            if result==False:
                result=self.isSubtree(s.right,t)
        return result

    def equal_tree(self,a:TreeNode,b:TreeNode):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val!=b.val:
            return False
        return self.equal_tree(a.left,b.left) and self.equal_tree(a.right,b.right)