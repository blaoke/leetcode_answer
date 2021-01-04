#定义一个dp数组m+1*n+1维,dp[i][j]表示word1的前i个字母转换成word2的前j个字母所使用的最少操作,i指向word1，j指向word2
#若当前字母相同，则dp[i][j] = dp[i - 1][j - 1];否则进行一次增删替操作， 即:dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        if m*n==0:
            return m+n
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        #定义初始状态
        for i in range(n+1):
            dp[0][i]=i
        for j in range(m+1):
            dp[j][0]=j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[j-1]!=word2[i-1]:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                else:
                    dp[i][j]=dp[i-1][j-1]
        return dp[m][n]

a=Solution()
print(a.minDistance(word1 = "horse", word2 = "ros"))


