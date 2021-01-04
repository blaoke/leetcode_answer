# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#方法一:前序遍历,如果是空节点就用$代替
class Codec:
    def __init__(self):
        self.res=[]

    def serialize(self, root):
        def decode(root):
            if not root:
                self.res.append('$')
                return
            else:
                self.res.append(root.val)
                decode(root.left)
                decode(root.right)
        decode(root)
        return self.res
    def deserialize(self, data):
        root = TreeNode(self.res[0])
        def encode(res):
            data=self.res.pop(0)
            if data == '$':
                return None
            nodes = TreeNode(data)
            nodes.left = encode(res)
            nodes.right = encode(res)
            return nodes
        self.res=data
        return encode(self.res)

#方法二:层次遍历
class Codec:
    def serialize(self, root):
        stack=[root]
        res=[]
        while stack:
            top=stack.pop(0)
            if top:
                res.append(top.val)
                stack.append(top.left)
                stack.append(top.right)
            else:
                res.append('null')
        return res

    def deserialize(self, data):
        if data == [] or data[0] == 'null':
            return None
        res=data
        root=TreeNode(res.pop(0))
        stack=[root]
        while stack:
            node=stack.pop(0)
            #左节点
            top=res.pop(0)
            if top=='null':
                node.left=None
            else:
                node.left=TreeNode(top)
                stack.append(node.left)
            #右节点
            top=res.pop(0)
            if top=='null':
                node.right=None
            else:
                node.right=TreeNode(top)
                stack.append(node.right)
        return root




