class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        m,n=len(grid),len(grid[0])#搜索范围的高和宽
        if m==0:
            return 0
        island=0#岛屿数量
        visited=[[False for _ in range(n)]for _ in range(m)]#访问过的位置
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 表示寻找的4个方向
        def inarea(x,y):
            return m-1>=x>=0 and n-1>=y>=0
        def dfs(startx,starty):
            visited[startx][starty]=True
            for i in range(4):
                newx=startx+d[i][0]
                newy=starty+d[i][1]
                if inarea(newx,newy) and not visited[newx][newy] and grid[newx][newy]=='1':
                    dfs(newx,newy)
            return

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=='1':#如果当前访问的位置为陆地,并且没有被访问过
                    dfs(i,j)
                    island+=1
        return island

a=Solution()
a.numIslands(grid=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
