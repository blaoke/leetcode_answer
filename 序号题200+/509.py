#记忆化搜索-自顶而下解决问题
class Solution:
    def fib(self, N: int) -> int:
        memory=[-1 for _ in range(N+1)]#记忆计算过的febi数共n+1个
        if N==0:
            return 0
        if N==1:
            return 1
        if memory[N]==-1:
            memory[N]=self.fib(N-1)+self.fib(N-2)
        return memory[N]

a=Solution()
a.fib(N=30)

#自底向上解决问题
class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        if N==1:
            return 1
        memory=[-1 for _ in range(N+1)]
        memory[0]=0
        memory[1]=1
        for i in range(2,N+1):
            memory[i]=memory[i-1]+memory[i-2]
        return memory[N]