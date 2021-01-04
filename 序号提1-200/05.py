#使用动态规划解决,建立二维数组,如果s[i]和s[j]对应的元素相同,那么当前状态s[i:j]是否为回文子串依赖于dp[i+1][j-1]的状态
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        dp=[[False for _ in range(n)] for _ in range(n)] #定义dp数组
        max_len=1 #最长长度
        start=0 #开始下标
        for k in range(n):
            dp[k][k]=True #每一个单个元素都是长度为1的回文子串
        for j in range(n): #从列开始
            for i in range(0,j):
                if s[j]==s[i]:
                    if j-i+1<=3:#如果j和i的区间长度<=3,而这时两头又相同,所以不管中间什么元素,这个区间都是回文子串
                        dp[i][j]=True
                    else: #区间长度大于3时,当前状态依赖于去掉区间两头后的状态
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False
                if dp[i][j]==True:
                    lens=j-i+1
                    if lens>max_len:
                        max_len=lens
                        start=i
        return s[start:start+max_len]

