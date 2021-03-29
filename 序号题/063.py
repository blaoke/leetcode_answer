#不同路径2，路径中有一些障碍物
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        if m==0:
            return 0
        n=len(obstacleGrid[0])
        cur=[0]*(n+1) #这里多加一列，防止测试用例为一列的情况
        #下面这个for循环为 路径第一行初始化
        for j in range(n):
            if obstacleGrid[0][j]==0: #如果这个地方没有障碍，就设置路径为1
                cur[j+1]=1  #因为多了一列，所以为j+1
            if obstacleGrid[0][j]==1: #第一行初始化过程中，如果前面有一个障碍物，后面都走不通，所以路径都为0
                break

        for i in range(1,m): #从第二行开始
            for j in range(n): #从第一列开始，测试用例有一列的情况
                if obstacleGrid[i][j]==0:
                    cur[j+1]+=cur[j]
                else: #表示如果有障碍
                    cur[j+1]=0
        return cur[-1]