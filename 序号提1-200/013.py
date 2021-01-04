# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
#方法一：先求解每一个对应的值，然后将str中反例减掉即可
class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        b = {'IV': 2, 'IX': 2, 'XL': 20, 'XC': 20, 'CD': 200, 'CM': 200}
        sum=0
        for i in s:
            sum+=a.get(i)
        v=list(b.keys())
        for j in range(len(v)):
            if v[j] in s:
                sum-=b.get(v[j])
        print(sum)
a=Solution()
a.romanToInt(s='mcmxciv')

#方法二:从倒数第二个str开始，往前遍历，如果前一个str对应的值小于其值本身，就在sum中减去这个值
class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum=a[s[-1]]
        index=len(s)-2
        while index>=0:
            sum+=a[s[index]]
            if a[s[index]]<a[s[index+1]]:
                sum-=a[s[index]]*2
            index-=1
        return sum
        print(sum)

a=Solution()
a.romanToInt(s='MCMXCIV')



