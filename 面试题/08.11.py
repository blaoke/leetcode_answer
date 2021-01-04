#本题类似背包问题,用动态规划解决,dp[i][j] i表示选到i种硬币,j表示用选到的硬币表示的金额,可用动态规划解决
#方法一:用2维矩阵解决,使用的空间复杂度较大
class Solution:
    def waysToChange(self, n: int) -> int:
        coins=[1,5,10,25]
        dp=[[0 for _ in range(n+1)] for _ in range(len(coins)+1)]
        for r in range(1,len(coins)+1):  #表示用各种硬币凑成金额0都只有一种情况
            dp[r][0]=1
        for r in range(1,len(coins)+1):
            dp[r][1:]=dp[r-1][1:] #从二行开始复制上一行的状态
            for c in range(1,n+1):
                if c>=coins[r-1]: #如果当前金额大于当前硬币值
                    dp[r][c]+=dp[r][c-coins[r-1]]
        return dp[-1][-1]%1000000007 #题目要求取余数

#方法二:在方法一的基础上使用数组解决
class Solution:
    def waysToChange(self, n: int) -> int:
        coins=[1,5,10,25]
        dp=[0 for _ in range(n+1)]
        dp[0]=1 #金额为0时,硬币凑到金额方法只有一种
        for r in range(len(coins)):
            if coins[r]<=n:
                for c in range(coins[r],n+1):
                    dp[c]+=dp[c-coins[r]]
        return dp[-1]%1000000007



