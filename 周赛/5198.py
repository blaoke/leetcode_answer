# !////usr////bin//env// python 
# -*- coding:utf-8 -*-
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        def maxyue(a, b):#求a,b最大公因数
            if a < b:
                a, b = b, a
            while b != 0:
                a, b = b, a % b
            return a
        def lcm(m,n): #求m,n的最小公倍数
            return m*n//maxyue(m,n)
        def shu(n):
            return n//a+n//b+n//c-n//lcm(a,b)-n//lcm(a,c)-n//lcm(b,c)+n//lcm(lcm(a,b),c)
        l=1;r=2*10**9+1
        while(l<r):
            mid=(l+r+1)/2
            ind=shu(mid)
            if ind==n:
                l=mid
                break
            elif ind>n:
                r=mid-1
            elif ind<n:
                l=mid
        print(l-min(l%a,min(l%b,l%c)))
li=Solution()
li.nthUglyNumber(n = 7, a = 7, b =7, c = 7)
#范围太大，看其他解决方法


