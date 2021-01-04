class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        rem = [[0 for _ in range(n)] for _ in range(m)]
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 表示寻找的4个方向
        def back(i, j):
            rem[i][j] = 1
            for l in range(4):  # 向上下右左寻找新的方向
                newx = i + d[l][0]
                newy = j + d[l][1]
                if  inarea(newx, newy) and sums(newx, newy) <= k :  # 在范围内,并且没有被访问
                    if rem[newx][newy] == 0:  # 如果访问成功了的话
                        back(newx, newy)
            # return
        def inarea(i, j):  # 判断是否在范围内
            return 0 <= i<m and 0<=j<n
        def sums(i, j):  # 求坐标的每个位之和
            return sum(map(int, str(i) + str(j))) #ma'p
        back(0,0)
        sums = 0
        for i in range(len(rem)):
            sums += sum(rem[i])
        return sums
a=Solution()
print(a.movingCount(m=2,n=3,k=1))