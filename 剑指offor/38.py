#方法一:位置交换方法
class Solution:
    def permutation(self, s: str):
        s=list(s)
        res=[]
        n=len(s)
        if not s:
            return res
        def dfs(x):
            if x==n:
                res.append(''.join(s))
            dic=set() #引入字典存储之前遍历过的元素,下次交换的时候如果相同值的元素交换过就不用再交换
            for i in range(x,n):
                if s[i] in dic: #剪枝操作
                    continue
                dic.add(s[i])
                s[i],s[x]=s[x],s[i]
                dfs(x+1)
                s[i], s[x] = s[x], s[i]
            return res
        return dfs(0)
a=Solution()
print(a.permutation(s='aac'))

#方法二:从空元素开始不断添加元素
class Solution:
    def permutation(self, s: str):
        res = []
        n = len(s)
        if not s:
            return res
        def dfs(s,tmp):
            if len(tmp)==n:
                res.append(tmp)
            dic=set()
            for i,x in enumerate(s):
                if x in dic:#剪纸操作,如果这个位置之前已经有相同的元素,就跳过
                    continue
                dic.add(x)
                new_tmp=tmp+x
                dfs(s[:i]+s[i+1:],new_tmp)
            return res
        return dfs(s,'')
a = Solution()
print(a.permutation(s='aac'))
