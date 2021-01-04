#第一种方法,使用空间复杂度为m*n
class Solution:
    def maxValue(self, grid: [[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j!=0:
                    grid[i][j]=grid[i][j]+grid[i][j-1] #第一行的元素等于这个元素累加前面的元素
                elif j==0 and i!=0: #第一列的元素等于这个元素累加这个一列前面的元素
                    grid[i][j]=grid[i][j]+grid[i-1][j]
                elif i>0 and j>0: #除第一行和第一列外,其他行和列的元素都等于这个元素+max(上面/左边)
                    grid[i][j]=grid[i][j]+max(grid[i][j-1],grid[i-1][j])
        return grid[-1][-1] #返回右下角元素

#方法二:在方法一的基础上优化,其实这个空间复杂度可以降为n,即至于要一行
class Solution:
    def maxValue(self, grid: [[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=[grid[0][0] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if i==0 and j!=0:
                    res[j]=grid[i][j]+res[j-1]
                elif j==0 and i!=0:
                    res[j]=grid[i][j]+res[j]
                elif i!=0 and j!=0:
                    res[j]=grid[i][j]+max(res[j-1],res[j])
        return res[-1]