class Solution:
    def translateNum(self, num: int) -> int:
        num=str(num)
        n=len(num)
        if n<2:
            return n
        dp=[1 for _ in range(n+1)]
        for i in range(n-2,-1,-1):
            if 10<=int(num[i]+num[i+1])<=25:
                dp[i]=dp[i+1]+dp[i+2]
            else:
                dp[i]=dp[i+1]
        return dp[0]
a=Solution()
print(a.translateNum(num=12258))


