#旋转矩阵:与48题相同,首先将矩阵进行转置,然后将每一行进行反转
class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
            #matrix[i]=matrix[i][::-1]