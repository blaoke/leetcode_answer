class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        col=[False for _ in range(n)]#存储皇后排行在哪一列
        dia1=[False for _ in range(2*n-1)]#第一个对角线,个数都为2*n-1
        dia2=[False for _ in range(2*n-1)]#第二个对角线

        res=[]#存放最终结果
        row=[]#存放每一次皇后在第几列
        def generateboard(n,row):#将第几列的元素表示成题目要求的样子
            l=[]
            for i in range(n):
                l.append('.' * row[i]+'Q'+'.'*(n-row[i]-1))
            return l

        def putQueue(index,row:list):#index表示在摆放第几行的皇后,row表示将皇后放在第几列
            if index==n:
                res.append(generateboard(n,row))
                return
            for j in range(n):#将第index行的皇后放在第j列
                if not col[j] and not dia1[index+j] and not dia2[index-j+n-1]:#当前第index行j列这个位置,行,列及两个斜对角线上没有皇后
                    row.append(j)
                    col[j]=True
                    dia1[index+j]=True
                    dia2[index-j+n-1]=True
                    putQueue(index+1,row)
                    #接下来进行回溯
                    col[j] = False
                    dia1[index + j] = False
                    dia2[index - j + n - 1] = False
                    row.pop()
            return
        putQueue(0,row)
        print(res)
        return res
a=Solution()
a.solveNQueens(n=4)





