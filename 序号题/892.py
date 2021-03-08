class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ret=0 #返回结果
        m=len(grid)
        n=len(grid[0])
        def sums(n): #求每一个v对应的表面积
            if n>0:
                return 6*n-2*(n-1)
            else:
                return 0
        for i in range(m):
            for j in range(n):
                ret+=sums(grid[i][j])
                if j <n-1: #每一行的元素只处理与其右边元素中的最小值
                    ret-=min(grid[i][j],grid[i][j+1])*2
                if i<m-1: #每一列的元素只处理与其下边元素中的最小值
                    ret -= min(grid[i][j], grid[i+1][j]) * 2
        return ret