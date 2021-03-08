#方法一:回溯法解决
class Solution:
    def letterCombinations(self, digits: str) -> [str]: #digits为'23'时候
        public=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        if len(digits)==0:
            return res
        def dfs(digit:str,index):#digit表示字符串,index表示数字字符串的索引
            if index==len(digits):
                res.append(digit)
                return
            c = public[int(digits[index])]#第一次index=0时c表示'abc',index=1时c表示'def'
            for j in c:
                dfs(digit+j,index+1)
        dfs('',0)
        return res

#方法二:利用队列解决
class Solution:
    def letterCombinations(self, digits: str) -> [str]: #digits为'23'时候
        public = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        if len(digits)==0:
            return []
        lens=1
        stack=[i for i in public[int(digits[0])]]
        while lens<len(digits):
            for i in range(len(stack)):
                top=stack.pop(0)
                for j in public[int(digits[lens])]:
                    stack.append(top + j)
            lens += 1
        return stack






