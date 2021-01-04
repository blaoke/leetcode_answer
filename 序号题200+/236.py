class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack=[root]
        res=[]
        def dfs(root,stack):
            if not root:
                return
            stack.append(root)
            if root==p or root==q:
                res.append(stack)
            dfs(root.left,stack)
            dfs(root.right,stack)
            stack.pop() #回溯,恢复状态
        dfs(root,[])
        p_tree=res[0]
        q_tree=res[1]
        i=0
        while q_tree[i]==p_tree[i]:
            i+=1
        return q_tree[i-1]

