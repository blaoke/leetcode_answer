class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        m = len(grid)
        n = len(grid[0])  # 搜索范围的高和宽
        island = 0
        visited = [[False for _ in range(n)] for _ in range(m)]  # 访问过的位置
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 表示寻找的4个方向

        def inarea(x, y):
            return m - 1 >= x >= 0 and n - 1 >= y >= 0

        def dfs(startx, starty):
            visited[startx][starty] = True
            island=1
            for i in range(4):
                newx = startx + d[i][0]
                newy = starty + d[i][1]
                if inarea(newx, newy) and not visited[newx][newy] and grid[newx][newy] == 1:
                    island+=dfs(newx, newy)
            return island

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:  # 如果当前访问的位置为陆地,并且没有被访问过
                    island=max(island,dfs(i, j))
        return island

