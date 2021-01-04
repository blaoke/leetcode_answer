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
        return memory[N]% 1000000007