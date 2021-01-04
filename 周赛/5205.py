# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:
        arr=sorted(arr)+[0]
        a=1
        b=[]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                a=a+1
            else:
                b.append(a)
                a=1
        if len(b)==len(list(set(sorted(b)))):
            print('t')
            return True
        else:
            print('f')
            return False
a=Solution()
a.uniqueOccurrences(arr=[-17,19,-17,-17,19,2,19,-17,19,19,2,19,0,19,19])




