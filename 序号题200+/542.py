#利用bfs解决,创建一个队列,将值为0的坐标存入队列,将问题转化为从值为0的点出发,计算其他值不为0的距离
from collections import deque #引入队列
class Solution:
    def updateMatrix(self, matrix: [[int]]) -> [[int]]:
        m=len(matrix)
        n=len(matrix[0])
        memo=[[False for _ in range(n)] for _ in range(m)]
        stack=deque()
        def inarea(x,y):
            return 0<=x<m and 0<=y<n
        direction=[[1,0],[-1,0],[0,-1],[0,1]]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    stack.append([i,j])
                    memo[i][j]=True
        while stack:
            x,y=stack.popleft()
            for k in range(4):
                newx = x+ direction[k][0]
                newy = y + direction[k][1]
                if inarea(newx, newy):
                    if memo[newx][newy]==False:
                        matrix[newx][newy]=matrix[x][y]+1
                        stack.append([newx,newy])
                        memo[newx][newy] == True
        return matrix



