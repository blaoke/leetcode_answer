class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        m,n=len(board),len(board[0])#m,n分别表示board的高度和宽度
        visited=[[False for _ in range(n)] for _ in range(m)] #定义此位置时候访问过的数组
        d=[[-1,0],[0,1],[1,0],[0,-1]]#表示寻找的4个方向
        def inarea(x,y): #判断是否在board的边界内部
            return m>x>=0 and n>y>=0

        def newsearch(index,startx,starty):#index表示寻找word中第几个单词,startx,starty分别表示开始寻找的x和y坐标
            if index==len(word)-1:
                return word[index]==board[startx][starty]
            if word[index]==board[startx][starty]:
                visited[startx][starty] = True
                for i in range(4):#向上下右左寻找新的方向
                    newx=startx+d[i][0]
                    newy=starty+d[i][1]
                    if inarea(newx,newy) and not visited[newx][newy]: #在范围内,并且没有被访问
                        if newsearch(index+1,newx,newy): #如果访问成功了的话
                            return True
                visited[startx][starty] = False#回溯的时候要擦除已经访问过这一个位置
            else:
                return False
        #从m,n遍历每一个元素
        if m*n<len(word):
            return False
        for i in range(m):
            for j in range(n):
                if newsearch(0,i,j):
                    return True
        return False

a=Solution()
a.exist(board =[['A','B'],['C','D']],word='ABCD')
