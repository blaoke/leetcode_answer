#从右上角入手,首先如果该数字大于要查找的数字,就去除这个数字所在的列,即向左走
# 如果这个数字小于要查找的数字,就去除这个数字所在的行，即向下走
class Solution:
    def findNumberIn2DArray(self, matrix: [[int]], target: int) -> bool:
        m=len(matrix)
        if m==0:
            return False
        n=len(matrix[0])
        x=0
        y=n-1
        while x<m and y>=0:
            if matrix[x][y]==target:
                return True
            if matrix[x][y]>target:
                y-=1
            else:
                x+=1
        return False


