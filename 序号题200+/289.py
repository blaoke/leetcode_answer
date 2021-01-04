class Solution:
    def gameOfLife(self, board: [[int]]):
        m=len(board)
        n=len(board[0])
        board_new=[[0 for _ in range(n)] for _ in range(m)]
        def inarea(x,y): #定义边界区域
            return 0<=x<m and 0<=y<n
        direction=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for i in range(m):
            for j in range(n):
                sum_one=0 #统计8个方向1的个数
                for k in range(8):
                    newx=i+direction[k][0]
                    newy=j+direction[k][1]
                    if inarea(newx,newy):
                        if board[newx][newy]==1:
                            sum_one+=1
                if board[i][j]==1:
                    if sum_one==2 or sum_one==3:
                        board_new[i][j]=1
                if board[i][j]==0:
                    if sum_one==3:
                        board_new[i][j]=1
        return board_new

a=Solution()
print( a.gameOfLife(board=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))

#方法二:方法一使用了o(mn)的空间复杂度,下面方法空间复杂度为1
#如果活细胞变为死细胞就将这个值改为-1,如果死细胞变为活细胞,就将这个值改为2
class Solution:
    def gameOfLife(self, board: [[int]]):
        m=len(board)
        n=len(board[0])
        def inarea(x,y): #定义边界区域
            return 0<=x<m and 0<=y<n
        direction=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for i in range(m):
            for j in range(n):
                sum_one=0 #统计8个方向1的个数
                for k in range(8):
                    newx=i+direction[k][0]
                    newy=j+direction[k][1]
                    if inarea(newx,newy):
                        if abs(board[newx][newy])==1:
                            sum_one+=1
                if board[i][j]==1:
                    if sum_one<2 or sum_one>3:
                        board[i][j]=-1
                if board[i][j]==0:
                    if sum_one==3:
                        board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j]==-1:
                    board[i][j]=0
                if board[i][j]==2:
                    board[i][j]=1
        return board

a=Solution()
print( a.gameOfLife(board=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))
