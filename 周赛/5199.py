# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
# class Solution(object):
#     def smallestStringWithSwaps(self, s, pairs):
#
#
# li=S
# s = "dcab", pairs = [[0,3],[1,2],[0,2]]
class Solution(object):
    def fraction(self, cont):
        while len(cont)>2:
            cont=cont[0:-2]+[cont[-1]**-1+cont[-2]]
        if cont[0]!=0:
            n=cont[0]
            x=cont[1]
            print([int(n*x+1),int(x)])
        else:
            n=cont[1]**-1
            x=1
            print([int(n),x])


        # bo=float.as_integer_ratio(cont)
        # print(list(bo))

a=Solution()
a.fraction(cont=[0,0,3])

class Solution(object):
    def fraction(self, cont):
        while len(cont)>2:
            cont=cont[0:-2]+[cont[-1]**-1+cont[-2]]
        if cont[0]!=0:
            n=cont[0]
            x=cont[1]
            return [int(n*x+1),int(x)]
        else:
            n=cont[1]**-1
            x=1
            return [int(n),x]