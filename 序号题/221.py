#方法:从上到下从左到右遍历数组,将当前位置(i,j)作为正方形的右下角,如果当前值等于1,则当前位置的值dp(i,j)=min(dp(i-1,j-1),dp(i-1,j),dp(i,j-1))+1
#即右下角值等于左上,左,上,三个值中的最小值加1
class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        m=len(matrix) #行
        if m == 0:
            return 0
        n=len(matrix[0]) #列
        def in_area(x,y):
            return 1<=x<m and 1<=y<n
        res=0
        for i in range(0,m):
            for j in range(0,n):
                if in_area(i,j):
                    if int(matrix[i][j])==0:
                        matrix[i][j]=0
                        continue
                    if int(matrix[i][j])==1:
                        matrix[i][j]=min(int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i-1][j-1]))+1
                        res=max(res,matrix[i][j])
                else: #第一行和第一列的元素
                    res=max(int(matrix[i][j]),res)
        return res*res
