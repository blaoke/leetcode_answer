#方法一:回溯法,如果left<n,就添加'(',如果right<left,就添加')'
class Solution:
    def generateParenthesis(self, n: int):
        res=[]
        tmp=[]
        def backtrack(left,right,n):
            if right==left==n:
                res.append(''.join(tmp))
            if left<n:
                tmp.append('(')
                backtrack(left+1,right,n)
                tmp.pop() #回溯
            if right<left:
                tmp.append(')')
                backtrack(left,right+1,n)
                tmp.pop()
        return res
#方法二:深度优先搜索,
class Solution:
    def generateParenthesis(self, n: int):
        res=[]
        tmp=''
        def dfs(left,right,n,tmp):
            if left==right==n:
                res.append(tmp)
            if left<right: #如果右括号数大于左括号数,表示条件不成立,进行剪枝操作
                return
            if left<n:
                dfs(left+1,right,n,tmp+'(')
            if right<n:
                dfs(left,right+1,n,tmp+')')

        dfs(0,0,n,tmp)
        return res



