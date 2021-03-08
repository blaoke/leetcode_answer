#bfs思想,将所有的陆地同时开始向4个方向增加1,最后栈中的元素对应的值-1即为最长路径
from collections import deque #引入队列
class Solution:
    def maxDistance(self, grid: [[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        land=deque() #存储陆地的
        direction=[[-1,0],[0,1],[1,0],[0,-1]] #定义寻找的4个方向
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    land.append([i,j])
        def inarea(x,y):
            return 0<=x<m and 0<=y<n
        length=0
        while land:
            x,y=land.popleft()
            for k in range(4):
                newx=direction[k][0]+x
                newy=direction[k][1]+y
                if inarea(newx,newy) : #在范围内
                    if grid[newx][newy]==0: #新区域为海洋,
                        length=1
                        grid[newx][newy]=grid[x][y]+1
                        land.append([newx,newy])
                else :
                    continue
        if length==0: #如果没有海洋,返回-1
            return -1
        return grid[x][y]-1


a=Solution()
print( a.maxDistance(grid=[[0,0,1,1,1],[0,1,1,0,0],[0,0,1,1,0],[1,0,0,0,0],[1,1,0,0,1]]))

