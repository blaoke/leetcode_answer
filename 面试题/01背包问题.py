#自底向上解决问题
#时间和空间复杂度都是o(n*c)
class Solution:
    def minWindow(self,w:list, v:list ,c:int ):#w表示各个物品重量,v表示价值,c表示剩余体积
        n=len(w)
        if n==0:
            return 0
        memo=[[-1 for _ in range(c+1)] for _ in range(n)]#动态规划需要的数组

        for j in range(c+1):#j表示这个背包的容量
            memo[0][j]=v[0] if j>=w[0] else 0 #背包中能放进第0号物品就加入,否则等于0

        for i in range(1,n):#从[1,n)逐行解决问题
            for j in range(c+1):#每一行逐列遍历
                memo[i][j]=memo[i-1][j]
                if j>=w[i]:#如果第i个物品能放进背包
                    memo[i][j]=max(memo[i][j],v[i]+memo[i-1][j-w[i]]) #将第i号为物品不放入和将i号物品放入并改变剩余容量这两种策略
        return  memo[n-1][c]
#在方法一的基础上令空间复杂度为o(2*c)
class Solution:
    def minWindow(self,w:list, v:list ,c:int ):#w表示各个物品重量,v表示价值,c表示剩余体积
        n=len(w)
        if n==0:
            return 0
        memo=[[-1 for _ in range(c+1)] for _ in range(2)]#动态规划需要的数组

        for j in range(c+1):#j表示这个背包的容量
            memo[0][j]=v[0] if j>=w[0] else 0 #背包中能放进第0号物品就加入,否则等于0

        for i in range(1,n):#从[1,n)逐行解决问题
            for j in range(c+1):#每一行逐列遍历
                memo[i%2][j]=memo[(i-1)%2][j]
                if j>=w[i]:#如果第i个物品能放进背包
                    memo[i%2][j]=max(memo[i%2][j],v[i]+memo[(i-1)%2][j-w[i]]) #将第i号为物品不放入和将i号物品放入并改变剩余容量这两种策略
        return  memo[n-1][c]

#在上面的基础上令空间复杂度为o(1*c),即用一行解决,不同点在于从右向左遍历
class Solution:
    def minWindow(self,w:list, v:list ,c:int ):#w表示各个物品重量,v表示价值,c表示剩余体积
        n=len(w)
        if n==0:
            return 0
        memo=[-1 for _ in range(c+1)] #动态规划需要的数组,定义为1行

        for j in range(c+1):#j表示这个背包的容量
            memo[j]=v[0] if j>=w[0] else 0 #背包中能放进第0号物品就加入,否则等于0

        for i in range(1,n):#从[1,n)逐行解决问题
            j=c
            while j>=w[i]:#从右向左,一直到能考虑的最小的物品
                memo[j] = max(memo[j], v[i] + memo[j - w[i]])  # 将第i号为物品不放入和将i号物品放入并改变剩余容量这两种策略
                j-=1
        return  memo[c]
