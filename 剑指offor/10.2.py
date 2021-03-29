class Solution:
    def numWays(self, n: int) -> int:
        memo=[i for i in range(n+1)]
        if n==0:
            return 1
        if n<3:
            return memo[n]
        for i in range(3,n+1):
            memo[i]=memo[i-1]+memo[i-2]
        return memo[n]%1000000007

# easy方法:
class Solution:
    def numWays(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        pre1=1
        pre2=1
        for i in range(n-1):
            res=pre1+pre2
            pre1,pre2=pre2,res
        return res%1000000007


