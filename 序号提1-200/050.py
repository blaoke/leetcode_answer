class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        if x==0: #如果底数为0,结果就为0
            return 0
        if n==0: #如果幂次数为0,结果就为1
            return 1
        res=1
        if n<0: #如果求的幂为负数,就转换为求其倒数的正数次幂
            x=1/x #取倒数
            n=-n
        while n!=1:
            if n%2!=0:#如果是奇数次幂  可以改成 if n&1
                res*=x #奇数次幂就保存一个底
            x*=x
            n=n//2
        return res*x

a=Solution()
print(a.myPow(x=2.0,n=10))