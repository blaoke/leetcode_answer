class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        start = 0 #开始的位置坐标,每一次开始的横坐标都等于纵坐标
        res=[] #存储返回结果
        m = len(matrix)  # 行数
        if m==0:
            return res
        n = len(matrix[0])  # 列数
        if n == 0:
            return res
        def circle(start):
            endx=m-1-start #结束的行坐标
            endy=n-1-start #结束的列坐标

            if start<=endy: #表示可以向右
                for i in range(start,endy+1):
                    res.append(matrix[start][i])

            if start<endx: #表示可以向下
                for j in range(start+1,endx+1):
                    res.append(matrix[j][endy])

            if start<endy and start<endx: #表示可以向左
                for k in range(endy-1,start-1,-1):
                    res.append(matrix[endx][k])

            if endx-start>=2 and start<endy: #表示可以向上
                for q in range(endx-1,start,-1):
                    res.append(matrix[q][start])

        while m>start*2 and n>start*2: #如果开始坐标x,y的2倍分别小于m和n就继续
            circle(start)
            start+=1
        return res