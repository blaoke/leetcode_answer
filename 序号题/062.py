#动态规划求解
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        broad=[[1 for i in range(n)] for _ in range(m)]
        for i in range(1,m):#遍历每一行
            for j in range(1,n):#遍历每一列
                broad[i][j]=broad[i-1][j]+broad[i][j-1]
        return broad[m-1][n-1]

a=Solution()
print(a.uniquePaths(m=3,n=2))

#大佬的方法
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n#只使用一行解决问题,每一次都不断更新这一行
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]