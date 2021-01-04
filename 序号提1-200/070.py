#利用组合方法
class Solution:
    def climbStairs(self, n: int) -> int:
        ci=n//1#i表示最多可以有多少个2阶台阶
        sum=0
        for i in range (ci):
            num=1
            for j in range(i):
                num*=(n-i-j)/(j+1)#选择排序的计算方法
            sum=sum+num
        print(int(sum))
s=Solution()
s.climbStairs(n=1)

#利用记忆搜索,自顶向下
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        memo=[-1 for i in range(n+1)]#存储记忆搜索的数组
        if memo[n]==-1:
            memo[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return memo[n]

#动态规划,自底向上
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        memo = [1 for i in range(n + 1)]  # 存储记忆搜索的数组
        for i in range(2,n+1):
            memo[i]=memo[i-1]+memo[i-2]
        return memo[n]