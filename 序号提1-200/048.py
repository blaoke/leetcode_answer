# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
#方法一：寻找规律，找到matrix[j][a-1-i]=matrix[i][j]，利用次方法建立一个新的矩阵b，然后填入，但是方法不满足题目要求，不能建立新的矩阵
import numpy as np
class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        a=len(matrix)
        b=np.ones((a,a))
        for i in range(a):
            for j in range(a):
                b[j][a-1-i]=matrix[i][j]
        print(b)
a=Solution()
a.rotate(matrix=[[1,2,3,8],[4,5,5,6],[1,7,8,9],[2,3,6,5]])

#方法二：利用np的.T转置方法先将矩阵转置，然后每一行进行调换，运行没问题，但是提交通过不了
import numpy as np
class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        matrix = np.array(matrix).T
        matrix=matrix.tolist()#将ndarray转换为list类型
        for i in range(len(matrix)):
            matrix[i].reverse()
        print(matrix)

#方法三：方法二的简洁版
import numpy as np
class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        matrix[:] = np.array(matrix).T
        print(list(matrix[:][i][::-1] for i in range(len(matrix[:]))))

#方法四：正确版本，先将矩阵转置然后每一行调换
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i]=matrix[i][::-1]
        return matrix
#方法四：方法一的正确版本，利用matrix[j][a-1-i]=matrix[i][j]进行连续4次转换，第一个值利用临时值tmp保存。
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])        
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp



