# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
#丑数
class Solution(object):
    def isUgly(self, num):
        if num<1:
            return False
        while num%2==0:
            num/=2
        while num%3==0:
            num/=3
        while num%5==0:
            num/=5
        return num==1



