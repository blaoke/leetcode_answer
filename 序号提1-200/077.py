class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        res=[]
        if n<1 or k>n or k<1:
            return res
        def dfs(ll:list,start):#ll表示向下迭代的列表,index表示列表中元素的个数,start表示线下迭代的开始范围
            if len(ll)==k:
                res.append(ll.copy())
                return
# 这个地方本来是[start,n+1),根据题意可以进行剪枝操作,需要k个元素,当前已经有len(ll)个元素,当前需要从i到n之间寻找k-len(ll)个元素,所以这个i与n的距离最多到n-(k-len(ll))+1就可以了
            for i in range(start,n-(k-len(ll))+2):
                ll.append(i)
                dfs(ll,i+1)
                ll.pop()#在向后回溯的时候要将添加的元素返回

        ll=[]
        dfs(ll,1)
        return res