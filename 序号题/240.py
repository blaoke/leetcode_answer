class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        if m==0:
            return False
        n=len(matrix[0])
        x=0 #行
        y=n-1 #列
        while x<m and y>=0:
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                y-=1
            else:
                x+=1
        return False
