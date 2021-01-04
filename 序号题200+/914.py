#方法一:自己方法
class Solution:
    def hasGroupsSizeX(self, deck: [int]) -> bool:
        import collections
        ret={}
        n=len(deck)
        if n<2:
            return False
        for i in range(n):
            ret[deck[i]]=ret.get(deck[i],0)+1
        #上面统计个数何以用 ret=collections.Counter(deck)

        a=min(ret.values())
        def gcd(x,y):
            small=min(x,y)
            while small:
                if x%small==0 and y%small ==0:
                    return small
                else:
                    small-=1
        #上面求最大公约数的函数可以用math.gcd()
        for j in ret.values():
            a=gcd(j,a)
        return a>1
a=Solution()
print(a.hasGroupsSizeX(deck=[1,1,2,2,2,2]))

#官方方法:
class Solution:
    def hasGroupsSizeX(self, deck: [int]) -> bool:
        import math
        from functools import reduce #functools.reduce逐次对上次函数结果与当前序列元素应用函数
        import collections
        ret = collections.Counter(deck).values()
        return reduce(math.gcd,ret)>=2

