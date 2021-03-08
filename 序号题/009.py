# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            print('false')
        elif x>=0:
            x=str(x)
            x1=len(x)
            x2=','.join(x).split(',')
            start=x2[:x1//2] if x1%2==0 else x2[:x1//2]
            end=x2[x1//2:] if x1%2==0 else x2[x1//2+1:]
            return  start==end[::-1]
a=Solution()
a.isPalindrome(x=1001)
