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


#上面方法使用了On的空间复杂度，可以使用O1的空间复杂度
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        pre1=0
        pre2=1
        for i in range(n-1):
            res=pre1+pre2
            pre1,pre2=pre2,res
        return res%1000000007
a=Solution()
print(a.numWays(n=7))