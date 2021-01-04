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